#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:44:28 2020

@author: orybchuk

Check if missing any ERA5 intermediate files
"""


import os
from datetime import datetime, timedelta

### Files to check
interm_dir = '/shared-projects/wps-inputs/metfiles/era5-grib/north-america/wrf_intermediate/'
sdate_str = '1998-12-01'
edate_str = '2019-01-01'
sdate = datetime.strptime(sdate_str, '%Y-%m-%d')
edate = datetime.strptime(edate_str, '%Y-%m-%d')

### Check files
missing_files = []
missing_dir = []
mydate = sdate
while mydate < edate:
    year = mydate.year
    month = mydate.month
    day = mydate.day
    
    monthdir = interm_dir+str(year)+'/'+str(month).zfill(2)+'/'
    for i in range(24):
        fname1 = 'ERA5_PRES:'+str(year)+'-'+str(month).zfill(2)+'-'\
                    +str(day).zfill(2)+'_'+str(i).zfill(2)
        fname2 = 'ERA5_SURF:'+str(year)+'-'+str(month).zfill(2)+'-'\
                    +str(day).zfill(2)+'_'+str(i).zfill(2)
        if not os.path.isfile(monthdir+fname1):
            missing_files.append(fname1)
            if monthdir not in missing_dir:
                missing_dir.append(monthdir)
        if not os.path.isfile(monthdir+fname2):
            missing_files.append(fname2)
            if monthdir not in missing_dir:
                missing_dir.append(monthdir)
        
    mydate += timedelta(days=1)
    
if len(missing_files) == 0:
    print("No missing files!")
else:
    print("Missing files in:")
    print(missing_dir)
