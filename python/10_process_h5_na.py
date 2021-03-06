### This script receives the region name as a parameter and completes the required fields
### in the master namelist.wps file

import h5py
import numpy as np
import pandas as pd
import pickle as pk
import os
import glob
import sys

# Read in WPS and WRF name
wps = sys.argv[1]
wrf = sys.argv[2]

root_dir = '/projects/oswwra/tap/region-offshoreNA/'
out_dir = '/projects/oswwra/obs_data/na/processed/'

obs_dict = pk.load(open(out_dir + '/buoy_na_hourly_h5_index.p', "rb"))

mod_dict = {}

wrf_vars = ['friction_velocity_2m', 
            'inversemoninobukhovlength_2m', 
            'roughness_length', 
            'windspeed_10m',
            'windspeed_20m',
            'windspeed_40m',
            'windspeed_60m',
#            'temperature_10m',
            'temperature_40m',
            'temperature_60m']

mod_df = pd.DataFrame(index = pd.date_range('2017-01-01 00:00:00', '2017-12-31 23:00:00', freq = 'H'),
                      columns = wrf_vars)

for site_id in obs_dict.keys():
    #mod_dict[site_id] = mod_df
    mod_dict[site_id] = pd.DataFrame()
#    print(mod_dict[site_id])


    
h5_file = '%s%s/h5/%s-%s_2017.h5' % (root_dir, wps, wps, wrf,)
print(h5_file)
if os.path.exists(h5_file):
    f = h5py.File(h5_file, 'r')
    meta = pd.DataFrame(f['time_index'][...], columns = ['time'])
    time_index = pd.to_datetime(meta['time'].str.decode("utf-8"))
       
    for site_id, obs_data in obs_dict.items():
       df_temp = pd.DataFrame(index=time_index)
       coord_loc = obs_data[1]
       for var in wrf_vars:
           ds = f[var]
           scale_factor = ds.attrs['scale_factor']
           df_temp[var] = ds[:, coord_loc] / scale_factor
       df_hourly = df_temp.resample("H").mean()
            #print(site_id, coord_loc)
            #print(df_hourly.values)
       mod_dict[site_id] = mod_dict[site_id].append(df_hourly)#.loc[df_hourly.index, wrf_vars] = df_hourly.values

    pk.dump(mod_dict, open(out_dir+'%s_%s_mod_data.p' % (wps, wrf,), 'wb'))
