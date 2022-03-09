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

fields = ['ws', 'wd', 'th1', 'th2', 'power']

# Now loop through all processed pickle files to grab needed
# data
df = pd.DataFrame()
for r in run_types:
    wrf_files = glob.glob('/shared/processed/%s*.p' % r)
    for w in wrf_files:
        #print(w)
        dt = w.split('.')[0][-19:]
        dtime = pd.to_datetime(dt, format = '%Y-%m-%d_%H:%M:%S')
        d = pk.load(open(w, 'rb'))
        for f in fields:
            dtemp = d[f]
            dsub = dtemp[lat_ran, lon_ran].values
            if f=='power':
                dfinal = dsub.sum()/1e6
            else:
                dfinal = dsub.mean()
                 
            df.loc[dtime, '%s_%s' %(r,f,)] = dfinal
        #print(df)
    df.sort_index(inplace = True)
    df.to_csv('/shared/processed/power_ts.csv')
