import pandas as pd
import pickle as pk
import glob

sites = ['test_loc']
ind_dir = '/home/moptis/temp/boem_atl_wrf_data/' 
#out_dir = /home/mpot

for s in sites:
    files = glob.glob(ind_dir + s + '*')
    print(files)
    df = pd.concat([pd.read_csv(f) for f in files])
    df.columns=df.columns.str.strip()
    print(df.columns)
    #df.sort_values(by = 'time', axis = 'columns')
    df['time'] = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M:%S')
    df.set_index('time', inplace = True)
    df.sort_index(inplace = True)#ascending = True)#'time', ascending = True, axis = 1)
    #print(type(combined_csv))
    #print(combined_csv.columns)
    df.to_csv('/home/moptis/temp/boem_test_loc.csv', index = True)
