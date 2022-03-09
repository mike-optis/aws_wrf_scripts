### This script receives the region name as a parameter and completes the required fields
### in the master namelist.wps file

import h5py
import numpy as np
import pandas as pd
import pickle as pk
import os
import glob
import sys
from operational_analysis.toolkits import met_data_processing

# Read in WPS and WRF name
wps = sys.argv[1]
#wps = ['WPS1']
#wrf = ['WRF1']
wrf = sys.argv[2]

root_dir = '/projects/oswwra/tap/region-offshoreCA/'
out_dir = '/projects/oswwra/obs_data/ca/processed/'

obs_dict = pk.load(open(out_dir + '/validation_data_hourly_h5_index.p', "rb"))

mod_dict = {}

def mo_name(month):
    if month<10:
        return '0'+str(month)
    else:
        return str(month)

months = [mo_name(m) for m in np.arange(1,13)]

wrf_vars = ['friction_velocity_2m', 
            'inversemoninobukhovlength_2m', 
            'roughness_length', 
            'windspeed_10m',
            'windspeed_40m',
            'windspeed_60m',
            'windspeed_100m',
#            'temperature_10m',
#            'temperature_2m',
            'temperature_40m',
#            'temperature_60m'
            'winddirection_10m'
            ]

mod_df = pd.DataFrame(index = pd.date_range('2017-01-01 00:00:00', '2017-12-31 23:00:00', freq = 'H'),
                      columns = wrf_vars)

for site_id in obs_dict.keys():
    #mod_dict[site_id] = mod_df
    mod_dict[site_id] = pd.DataFrame()
#    print(mod_dict[site_id])

for m in months:
    
    h5_file = '%s%s/h5_new/%s-%s_2017-%s.h5' % (root_dir, wps, wps, wrf, m,)
    #h5_file = '%sWPS1/h5_new/WPS1-WRF1_2017-%s.h5' % (root_dir, m)
    print(h5_file)
    if os.path.exists(h5_file):
        f = h5py.File('%s%s/h5_new/%s-%s_2017-%s.h5' % (root_dir, wps, wps, wrf, m,), 'r')
        #f = h5py.File('%sWPS1/h5_new/WPS1-WRF1_2017-%s.h5' % (root_dir, m), 'r')
        meta = pd.DataFrame(f['time_index'][...], columns = ['time'])
        time_index = pd.to_datetime(meta['time'].str.decode("utf-8"))
       
        for site_id, obs_data in obs_dict.items():
            df_temp = pd.DataFrame(index=time_index)
            coord_loc = obs_data[1]
            for var in wrf_vars:
                print('Processing variable ' + var)
                #ds = f[var]
                #scale_factor = ds.attrs['scale_factor']
                #df_temp[var] = ds[:, coord_loc] / scale_factor
                if (var == 'winddirection_10m'):
                    wspd = f['windspeed_10m']
                    wspd_scale = wspd.attrs['scale_factor']
                    wind_spd = wspd[:, coord_loc] / scale_factor
                    wdir = f[var]
                    wdir_scale = wspd.attrs['scale_factor']
                    wdir_temp = df_temp.copy()
                    wdir_temp[var] = wdir[:, coord_loc] / wdir_scale
                    u, v = met_data_processing.compute_u_v_components(wind_spd, wdir_temp[var])
                    #u_avg = u.resample("H").mean()
                    #v_avg = v.resample("H").mean()
                    df_temp['u_wnd'] = u
                    df_temp['v_wnd'] = v
                    #wdir_final = met_data_processing.compute_wind_direction(u_avg, v_avg)
                    #if (var == 'winddirection_10m'):
                    #mod_dict[site_id] = mod_dict[site_id].append(wdir_final)
                else:
                    ds = f[var]
                    scale_factor = ds.attrs['scale_factor']
                    df_temp[var] = ds[:, coord_loc] / scale_factor
                    #df_hourly = df_temp.resample("H").mean()
                    #print(site_id, coord_loc)
                    #print(df_hourly.values)
                    #mod_dict[site_id] = mod_dict[site_id].append(df_hourly)#.loc[df_hourly.index, wrf_vars] = df_hourly.values
            if (var == 'winddirection_10mdd'):
               mod_dict[site_id] = mod_dict[site_id].append(wdir_final)
            else:
               df_hourly = df_temp.resample("H").mean()
               # Now we can calculate actual wind direction
               wdir_final = met_data_processing.compute_wind_direction(df_hourly['u_wnd'], df_hourly['v_wnd'])
               df_hourly['winddirection_10m'] = wdir_final
               mod_dict[site_id] = mod_dict[site_id].append(df_hourly)

        pk.dump(mod_dict, open(out_dir+'%s_%s_mod_data_wdir.p' % (wps, wrf,), 'wb'))

print('All done!')
