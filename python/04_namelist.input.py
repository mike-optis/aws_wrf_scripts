
import pandas as pd
import sys
import os
import numpy as np
from calendar import monthrange
import sys

domain = sys.argv[1]
type = 'all_farms'
root_dir = "/mys3bucket/wrf_runs/%s/" % domain

mo_df = pd.read_csv('/mnt/efs/fs1/key_inputs/model_months.csv')
df = mo_df.loc[mo_df['windfarm'] == domain]

#year = int(sys.argv[2])
#month = int(sys.argv[3])
#type = sys.argv[4]

# Turn integer month into string
def ID(x):
    if x < 10:
        return '0'+ str(x)[0:1]
    else:
        return str(x)[0:2]

dir = '001' # starting directory
for n in np.arange(0,12):
    year = df.loc[n, 'year']
    month = df.loc[n, 'month']
    dpm = monthrange(year, month)[1]
    st_date = pd.datetime(year, month, 1, 0, 0) - pd.Timedelta(1, 'D') + pd.Timedelta(12, 'H')# Spin up on last day of month at 12th hour
    en_date = pd.datetime(year, month, 1, 0, 0) + pd.Timedelta(2, 'D') # 2-day sim with 12 hour start up 
    final_end = pd.datetime(year, month, 1, 0, 0) + pd.Timedelta(dpm, 'D') #+ pd.Timedelta(2, 'D') # Where we stop plus one day buffer
    print(final_end)

    while en_date <= final_end:
        end_diff = pd.Timedelta(final_end - en_date).days
        if end_diff < 2:
           en_date = final_end
            #en_date = final_end #en_date - pd.Timedelta(1, 'D') # make sure we terminate on the first of the next month
        #    print('yes')
           print(dir, st_date, en_date)
        #print(st_date, en_date, pd.Timedelta(final_end - en_date).days)
       # Open master namelist file and make the replacement
        dirpath = root_dir + '/%s/' % type + dir
        print(dirpath)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        with open('/mnt/efs/fs1/namelists/namelist.input.template.%s' % domain, 'r') as file:
            filedata = file.read()
        
            # Write start and end dates
            filedata = filedata.replace('yst', str(st_date.year)) 
            filedata = filedata.replace('mst', ID(st_date.month))
            filedata = filedata.replace('dst', ID(st_date.day))                                                                                                  
            filedata = filedata.replace('yend', str(en_date.year))
            filedata = filedata.replace('mend', ID(en_date.month))
            filedata = filedata.replace('dend', ID(en_date.day))
            filedata = filedata.replace('hsty', str(year))
            filedata = filedata.replace('hstm', ID(month))        
            filedata = filedata.replace('rn_type', type)        

            with open('%s/%s/%s/namelist.input' % (root_dir,type,dir,), 'w') as file:
                file.write(filedata)
	
            # Update directory
            st_date = st_date + pd.Timedelta(2, 'D')
            en_date = en_date + pd.Timedelta(2, 'D')
            dir = str(int(dir) + 1).zfill(3)
