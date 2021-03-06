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
wps = 'WPS1'
wrf = 1
year = sys.argv[1]

root_dir = '/projects/oswwra/tap/prod-offshoreCA/'
out_dir = '/home/moptis/temp/boem_atl_wrf_data/'

# Load example h5 data
h5_file = root_dir + 'h5_bad/20yr/Offshore_CA_%s.h5' % str(year)
f = h5py.File(h5_file, 'r')

coordinates = f['coordinates']

# Match two lidar locations to WRF h5 index
obs_dict = {'test_loc': [40.042, -124.528]
           # 'lidar_e06': [39.55, -73.43]
            }


for obs_site, obs_data in obs_dict.items():
    lat_target = obs_data[0]
    lon_target = obs_data[1]
    coord_loc = np.argmin(np.abs(coordinates[:,0] - lat_target) + np.abs(coordinates[:,1] - lon_target))
    print(coord_loc)
    obs_data.append(coord_loc)
print(obs_dict)

wrf_vars = [#'friction_velocity_2m', 
            #'inversemoninobukhovlength_2m', 
            #'surface_sea_temperature',
            #'surface_heat_flux',
            #'roughness_length', 
            #'windspeed_10m',
            #'windspeed_20m',
            #'windspeed_40m',
            #'windspeed_60m',
            'windspeed_100m'#,
            #'windspeed_120m',
            #'windspeed_140m',
            #'windspeed_160m',
            #'windspeed_200m',
            #'temperature_2m']
]


if os.path.exists(h5_file):
    print(h5_file)
    
    meta = pd.DataFrame(f['time_index'][...], columns = ['time'])
    time_index = pd.to_datetime(meta['time'].str.decode("utf-8"))
    for site_id, obs_data in obs_dict.items():
        df_temp = pd.DataFrame(index=time_index)
        coord_loc = obs_data[2]
        for var in wrf_vars:
            print(site_id, var)
            ds = f[var]
            scale_factor = ds.attrs['scale_factor']
            df_temp[var] = ds[:, coord_loc] / scale_factor
        #df_temp = df_temp.loc[df_temp.index.year==2019]
        df_temp.to_csv(out_dir + site_id + '_' + str(year) + '.csv')

