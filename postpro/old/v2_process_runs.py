# Code to process raw WRF results into 80m wind speed
# and direction, which is saved as a pickle file

from netCDF4 import Dataset
from wrf import getvar, interplevel, latlon_coords
import glob
import pickle as pk
import numpy as np
import multiprocessing as mp
import pandas as pd
import sys
import os
import json
from functools import partial

def process_wrf(k):
    #print(n)
    d = str(k).zfill(3)
    for r in ['all_farms', 'target_only']:
        print(r)
        st_date = pd.to_datetime(domain_indices.loc[k]) + pd.Timedelta(1, 'D')
        #print('done st_date')
        #print(domain, st_date)
        data_dict = {}
        #run_dir = '/shared/%s/%s/' % (r, d)
        run_dir = '/mnt/mys3/wrf_runs/%s/%s/%s/' % (domain,r,d)
        #print(run_dir)
        #save_dir = '/shared/processed/'
        save_dir = '/mnt/mys3/processed_results/%s/' % domain

        # Get list of wrf output files
        ncfiles = glob.glob('%s/wrfout_d02*' % run_dir)
        #print(n)
        #print(ncfiles)
        for i,n in enumerate(ncfiles):
            #print(i,n)
        #for p in [0]:
            try:
                date_str = n.split('/')[-1][11:]
                dt = pd.to_datetime(date_str, format = "%Y-%m-%d_%H:%M:%S")   
                print(k, r, st_date, dt)
                save_file = "%s/%s_%s.p" % (save_dir, r, date_str,)
                if (dt>=st_date) & (not os.path.exists(save_file)):
                    #print(st_date, dt)
                    ncfile = Dataset(n)
                    print('loaded')
                    ws = getvar(ncfile, "uvmet_wspd")
                    wd = getvar(ncfile, "uvmet_wdir")
                    pw = getvar(ncfile, "POWER")
                    th = getvar(ncfile, "theta")
                    th1 = getvar(ncfile, "wspd_wdir10")[0,:,:]
                    h = getvar(ncfile, "height_agl")
                    lats, lons = latlon_coords(h)
                    times = getvar(ncfile, 'xtimes')
                    tm = int(times.values)
                    ws_hh = interplevel(ws, h, ws_height) # Hub height wind speed
                    wd_hh = interplevel(wd, h, ws_height) # Hub height wind direction
                    th2 = interplevel(th, h, th_height2) # top pot. temp.
                    #th1 = interplevel(th, h, th_height1) # lower pot. temp.

                    data_dict['ws'] = ws_hh
                    data_dict['wd'] = wd_hh
                    data_dict['th2'] = th2
                    data_dict['th1'] = th1
                    data_dict['power'] = pw
               
                    pk.dump(data_dict, open( "%s/%s_%s.p" % (save_dir, r, date_str,), "wb" ) ) 
                    ncfile.close()
            except:
                print('corrupt')
        print('done')
    print('done2')
    
###########################################

domain = sys.argv[1]

run_indices = pd.read_csv('/shared/key_inputs/run_indices.csv', index_col = 0)
domain_indices = run_indices.loc[:, domain]

farm_file = open('/shared/key_inputs/farm_info.json', 'r')
farm_data = json.load(farm_file)
lat_ran = np.arange(farm_data[domain]['lat_min'],farm_data[domain]['lat_max'] + 1)
lon_ran = np.arange(farm_data[domain]['lon_min'],farm_data[domain]['lon_max'] + 1)
ws_height = farm_data[domain]['ws_height']
th_height1 = farm_data[domain]['th_height1']
th_height2 = farm_data[domain]['th_height2']


if __name__=='__main__':

    for m in np.arange(170,185,4):
        print(m)
        with mp.Pool(4) as p:
            print(p.map(process_wrf, np.arange(m,m+4)))
            #t = p.map(process_wrf, [2])
