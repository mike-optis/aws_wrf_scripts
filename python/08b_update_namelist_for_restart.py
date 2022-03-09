## Restarts a WRF run based on latest restart file
## Takes as input the run folder for WRF

import pandas as pd
import glob
import numpy as np
from calendar import monthrange
import sys
import os

run_dir = sys.argv[1]

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
    restart_list = glob.glob('%s/wrfrst_d02*' % run_dir)
    restart_list.sort() # Sort by date
    #print(restart_list)
    restart_date = pd.to_datetime(restart_list[-1][-24:-5], format = '%Y-%m-%d_%H:%M:%S') # Get last date

    ryr = str(restart_date.year) # Year
    rmo = ID(restart_date.month) # Month
    rday = ID(restart_date.day) # Day

    # Read in old namelist and split into list by line
    with open('%s/namelist.input' % run_dir, 'r') as file:
        namelist_old = file.read()
    namelist_split = namelist_old.split('\n')
    
    # Get old start dates
    yr_old = namelist_split[1][-5:-1]
    mo_old = namelist_split[2][-3:-1]
    day_old = namelist_split[3][-3:-1]
    
    # Replace old start dates with restart ones
    namelist_split[1] = namelist_split[1].replace(yr_old, ryr)
    namelist_split[2] = namelist_split[2].replace(mo_old, rmo)
    namelist_split[3] = namelist_split[3].replace(day_old, rday)

    # Set restart option to true if it isn't already
    if namelist_split[13][-7:-2] == 'false':
        namelist_split[13] = namelist_split[13].replace('false', 'true')

    # Now convert list back to string and resave
    namelist_new = '\n'.join(namelist_split)
    with open('%s/namelist.input' % run_dir, 'w') as file:
        file.write(namelist_new)

    # Now relaunch the runs
    os.chdir(run_dir)
    #os.system("sbatch submit_wrf.sh")
        
else:
    print('WRF simulation complete, no need to restart')
