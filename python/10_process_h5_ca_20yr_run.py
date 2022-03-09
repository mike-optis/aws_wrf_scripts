### This script receives the region name as a parameter and completes the required fields
### in the master namelist.wps file

import h5py
import numpy as np
import pandas as pd
import pickle as pk
import os
import glob
import sys

#root_dir = '/projects/oswwra/tap/region-offshoreCA/'
root_dir = '/projects/oswwra/tap/prod-offshoreCA/'
out_dir = '/projects/oswwra/obs_data/ca/processed/'

#obs_dict = pk.load(open(out_dir + '/02_validation_data_hourly_h5_index.p', "rb"))

mod_dict = {}

wrf_vars = [#'surface_sea_temperature',
            #'friction_velocity_2m', 
            #'inversemoninobukhovlength_2m', 
            #'roughness_length', 
            #'windspeed_10m',
            #'windspeed_40m',
            #'windspeed_60m',
            'windspeed_100m',
            #'windspeed_120m',
            #'windspeed_140m',
            #'windspeed_160m',
            #'windspeed_200m',
#            'temperature_10m',
            #'temperature_2m',
            #'temperature_40m',
#            'temperature_60m'
            #'winddirection_10m'
            ]

#mod_df = pd.DataFrame(index = pd.date_range('2017-01-01 00:00:00', '2017-12-31 23:00:00', freq = 'H'),
#                      columns = wrf_vars)

for site_id in obs_dict.keys():
    #mod_dict[site_id] = mod_df
    mod_dict[site_id] = pd.DataFrame()

for year in np.arange(2000, 2020):
#year = 2017
    h5_file = '%s/h5/20yr/Offshore_CA_%s.h5' % (root_dir, year,)
    print(h5_file)
    if os.path.exists(h5_file):
        f = h5py.File(h5_file, 'r')
        meta = pd.DataFrame(f['time_index'][...], columns = ['time'])
        time_index = pd.to_datetime(meta['time'].str.decode("utf-8"))
   
    for site_id, obs_data in obs_dict.items():
        df_temp = pd.DataFrame(index=time_index)
        coord_loc = obs_data[1]
        for var in wrf_vars:
            print(site_id, var)
            ds = f[var]
            scale_factor = ds.attrs['scale_factor']
            df_temp[var] = ds[:, coord_loc] / scale_factor
        df_hourly = df_temp.resample("H").mean()
        mod_dict[site_id] = mod_dict[site_id].append(df_hourly)#.loc[df_hourly.index, wrf_vars] = df_hourly.values

    #pk.dump(mod_dict, open(out_dir+'WPS%s_WRF%s_mod_data.p' % (wps, wrf,), 'wb'))