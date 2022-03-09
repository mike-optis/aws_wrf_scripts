######################################################
# Script to link the met data needed for real.exe
# for each of the folders in a specific directory
######################################################


import sys
import glob
import pandas as pd
import os

domain = sys.argv[1]
type = sys.argv[2]

run_dir = '/shared/%s/' % (type,)

dirlist = glob.glob(run_dir+'*')

# Loop through run directories
for d in dirlist:
    # Load namelist
    with open('%s/namelist.input' % d, 'r') as file:
        filedata = file.readlines()
        st_year = filedata[1].split('=')[1][1:5]
        st_mo = filedata[2].split('=')[1][1:3]
        st_day = filedata[3].split('=')[1][1:3]
        en_year = filedata[7].split('=')[1][1:5]
        en_mo = filedata[8].split('=')[1][1:3]
        en_day = filedata[9].split('=')[1][1:3]
        print(st_year, st_mo, st_day, en_year, en_mo, en_day)
        
        st_date = pd.to_datetime('%s-%s-%s' % (st_year, st_mo, st_day,), format = '%Y-%m-%d')
        en_date = pd.to_datetime('%s-%s-%s' % (en_year, en_mo, en_day,), format = '%Y-%m-%d')
        #print(st_date, en_date)

        dt_range = pd.date_range(st_date, en_date, freq = '3H')

        for dt in dt_range:
            str_dt = '%s-%s-%s_%s:00:00.nc' % (dt.year, str(dt.month).zfill(2), str(dt.day).zfill(2), str(dt.hour).zfill(2))
            met1_path = '/shared/met_data/all_met/met_em.d01.%s' % (str_dt,)
            met2_path = '/shared/met_data/all_met/met_em.d02.%s' % (str_dt,)
            os.chdir(d)
            os.system('ln -sf %s .' % met1_path)
            os.system('ln -sf %s .' % met2_path)


