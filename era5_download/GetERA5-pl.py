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

regions = {'tx_ok': [45, -120, 20, -85]}
#print(month)
#print(year)

def conv(x):
    if x>9:
        return str(x)
    else:
        return '0' + str(x)

#root_dir = '/home/era5_data/data/'
save_root = '/mnt/mys3/era5_data/'
save_dir = save_root + str(year) + '/' + conv(month) + '/' 

if not os.path.exists(save_dir):
    os.makedirs(save_dir, exist_ok = True)


c = cdsapi.Client()

#for day in [1]:
for d in np.arange(1, days_in_month+1):
    save_name = '%s/ERA5-pressure-%s-%s-%s.grib' % (save_dir, str(year), conv(month), conv(d),)
    print(save_name)
    if not os.path.isfile(save_name):
	    c.retrieve(
    		    'reanalysis-era5-pressure-levels',
    	    	{
        	'product_type':'reanalysis',
	        'format':'grib',
		 'pressure_level':[
   		         '1','2','3',
		            '5','7','10',
		            '20','30','50',
		            '70','100','125',
		            '150','175','200',
		            '225','250','300',
		            '350','400','450',
		            '500','550','600',
		            '650','700','750',
		            '775','800','825',
		            '850','875','900',
		            '925','950','975',
		            '1000'
        ],
        	'variable':[
			'geopotential','relative_humidity','specific_humidity',
			'temperature', 'u_component_of_wind', 'v_component_of_wind'
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
	        'area':  [61, -130, 20, -50],
	    },
    		'%s/ERA5-pressure-%s-%s-%s.grib' % (save_dir, str(year), conv(month), conv(d),)
	)

