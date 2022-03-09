import cdsapi
import sys
from calendar import monthrange
import numpy as np	
import os

year = int(sys.argv[1])
month = int(sys.argv[2])
#d = int(sys.argv[3])
days_in_month = monthrange(year, month)[1]
hours = np.arange(24)

#regions = {'tx_ok': [45, -120, 20, -85]}

#print(month)
#print(year)

def conv(x):
    if x>9:
        return str(x)
    else:
        return '0' + str(x)

#root_dir = '/home/era5_data/data/'
save_root = '/mys3bucket/era5_data/'
save_dir = save_root + str(year) + '/' + conv(month) + '/' 

if not os.path.exists(save_dir):
    os.makedirs(save_dir, exist_ok = True)


c = cdsapi.Client()

#for day in [1]:
for d in np.arange(1, days_in_month+1):
    save_name = '%s/ERA5-surface-%s-%s-%s.grib' % (save_dir, str(year), conv(month), conv(d),)
    print(save_name)
    if not os.path.isfile(save_name):
	    c.retrieve(
    		    'reanalysis-era5-single-levels',
    	    	{
        		'product_type':'reanalysis',
	       	 'format':'grib',
        		'variable':[
	        	    	'10m_u_component_of_wind','10m_v_component_of_wind','2m_dewpoint_temperature',
        	    		'2m_temperature','land_sea_mask','mean_sea_level_pressure',
	            		'sea_ice_cover','sea_surface_temperature','skin_temperature',
        	    		'snow_depth','soil_temperature_level_1','soil_temperature_level_2',
            			'soil_temperature_level_3','soil_temperature_level_4','surface_pressure',
            			'volumetric_soil_water_layer_1','volumetric_soil_water_layer_2','volumetric_soil_water_layer_3',
            			'volumetric_soil_water_layer_4'
	       	 ],
        		'year': str(year),
			'month': conv(month),
			'day': conv(d),
			'time': [
	     	       '00:00', '01:00', '02:00',
        		    '03:00', '04:00', '05:00',
	       	     '06:00', '07:00', '08:00',
	       	     '09:00', '10:00', '11:00',
	       	     '12:00', '13:00', '14:00',
	       	     '15:00', '16:00', '17:00',
	       	     '18:00', '19:00', '20:00',
	       	     '21:00', '22:00', '23:00',
	       	 ],
	        	'area': [61, -130, 20, -50],
	    },
    	'%s/ERA5-surface-%s-%s-%s.grib' % (save_dir, str(year), conv(month), conv(d),)
	)


