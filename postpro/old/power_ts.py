#Code to grab power data from processed dictionaries and create
# a final power time series for target wind farm

import glob
import pickle as pk
import numpy as np
import multiprocessing as mp
import pandas as pd
import sys
import numpy as np
import glob
import json
import os

#run_type = 'longhorn_only'
run_types = ['target_only', 'all_farms']
#run_types = ['all_farms']
domain = sys.argv[1]

# Read in wind farm indices for extraction
farm_file = open('/shared/key_inputs/farm_info.json', 'r')
farm_data = json.load(farm_file)
lat_ran = np.arange(farm_data[domain]['lat_min'],farm_data[domain]['lat_max'] + 1)
lon_ran = np.arange(farm_data[domain]['lon_min'],farm_data[domain]['lon_max'] + 1)
ws_height = farm_data[domain]['ws_height']
th_height1 = farm_data[domain]['th_height1']
th_height2 = farm_data[domain]['th_height2']
fs_lat = farm_data[domain]['fs_lat']
fs_lon = farm_data[domain]['fs_lon']

fields = ['ws', 'wd', 'th1', 'th2', 'power']
#fields = ['ws', 'wd', 'power']

# Now loop through all processed pickle files to grab needed
# data
df = pd.DataFrame()
for r in run_types:
    #wrf_files = glob.glob('/shared/processed/%s*.p' % r)
    for m in np.arange(1,13):
        wrf_files = glob.glob('/mnt/mys3/processed_results/%s/%s/%s*.p' % (domain,str(m).zfill(2),r,))
        for i,w in enumerate(wrf_files):
            #print(i,w)
            dt = w.split('.')[0][-19:]
            dtime = pd.to_datetime(dt, format = '%Y-%m-%d_%H:%M:%S')
            d = pk.load(open(w, 'rb'))
            for f in fields:
                dtemp = d[f]
            
                if f=='power':
                    dsub = dtemp[lat_ran, lon_ran].values
                    dfinal = dsub.sum()/1e6
                else:
                    dfinal = dtemp[fs_lat, fs_lon].values
                 
                df.loc[dtime, '%s_%s' %(r,f,)] = dfinal
        #print(df)
            if i%100 ==0:
                print(i,w)
                df.sort_index(inplace = True)
                df.to_csv('/shared/processed/power_ts.csv')
        df.sort_index(inplace = True)
        df.to_csv('/shared/processed/power_ts.csv')
