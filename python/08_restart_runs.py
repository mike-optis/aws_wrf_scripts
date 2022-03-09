## Restarts a WRF run based on latest restart file
## Takes as input the run folder for WRF

import pandas as pd
import glob
import numpy as np
from calendar import monthrange
import sys
import os
import shutil

run_dir = sys.argv[1]
save_dir = sys.argv[2]

dir_split = run_dir.split('/')

tstep = sys.argv[3]

offset = 1

month = dir_split[-2 + offset]
year = dir_split[-3 + offset]
wrf = dir_split[-4 + offset]
print(wrf, year, month)


# Turn integer month into string
def ID(x):
    if x < 10:
        return '0'+ str(x)[0:1]
    else:
        return str(x)[0:2]

# Check if WRF completed based on last line in rsl.out.0000
with open('%s/rsl.out.0000' % run_dir, 'r') as file:
    rsldata = file.read()[-30:-1]

if rsldata.find('SUCCESS COMPLETE WRF') == -1: # WRF run didn't complete
    # find the date of the last restart file
    restart_list = glob.glob('%s/wrfrst_d02*' % save_dir)
    restart_list_d01 = glob.glob('%s/wrfrst_d01*' % save_dir)
    restart_list.sort() # Sort by date
    restart_list_d01.sort()
    #print(restart_list)
    
    # Copy restart file to run directory
    os.system("cp %s %s" % (restart_list[-1], run_dir,))
    os.system("cp %s %s" % (restart_list_d01[-1], run_dir,))

    restart_date = pd.to_datetime(restart_list[-1][-19:], format = '%Y-%m-%d_%H:%M:%S') # Get last date
    print(restart_date)
    ryr = str(restart_date.year) # Year
    rmo = ID(restart_date.month) # Month
    rday = ID(restart_date.day) # Day
    rhour = ID(restart_date.hour) # Day
    print(rhour)

    # Read in old namelist and split into list by line
    with open('%s/namelist.input' % run_dir, 'r') as file:
        namelist_old = file.read()
    namelist_split = namelist_old.split('\n')
    
    # Get old start dates
    yr_old = namelist_split[1][-5:-1]
    mo_old = namelist_split[2][-3:-1]
    day_old = namelist_split[3][-3:-1]
    hour_old = namelist_split[4][-3:-1]

    # Get old time step
    tstep_old = namelist_split[35][-3:-1]
    print('old time step is %s' % tstep_old)
    print(namelist_split[35])
    
    # Replace old start dates with restart ones
    namelist_split[1] = namelist_split[1].replace(yr_old, ryr)
    namelist_split[2] = namelist_split[2].replace(mo_old, rmo)
    namelist_split[3] = namelist_split[3].replace(day_old, rday)
    namelist_split[4] = namelist_split[4].replace(hour_old, rhour)
    
    # Replace with new time step
    namelist_split[35] = namelist_split[35].replace(tstep_old, tstep)
    
    # Set restart option to true if it isn't already
    print(namelist_split[18][-7:-2])
    if namelist_split[18][-7:-2] == 'false':
        namelist_split[18] = namelist_split[18].replace('false', 'true')

    # Now convert list back to string and resave
    namelist_new = '\n'.join(namelist_split)
    with open('%s/namelist.input' % run_dir, 'w') as file:
        file.write(namelist_new)

    # Now relaunch the runs
    shutil.copyfile('/shared/scripts/bash/aws_cluster_launch.sh', '%s/aws_cluster_launch.sh'  % run_dir)
    os.chdir(run_dir)
    os.system("sbatch ./aws_cluster_launch.sh")
        
else:
    print('WRF simulation complete, no need to restart')
