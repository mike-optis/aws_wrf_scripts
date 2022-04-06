# Code to create wind deficit map and power deficit caused by 
# neighboring wakes. For now, we only work with Longhorn and
# pass the month in as input, assuming a 2020 run

# Mike Optis - 2021-11-30

import os
import pickle as pk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from netCDF4 import Dataset
from wrf import (to_np, getvar, smooth2d, get_cartopy, cartopy_xlim,
                 cartopy_ylim, latlon_coords)
from matplotlib.cm import get_cmap
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature
import cartopy.crs as ccrs
import sys
from calendar import monthrange
import glob

#month = sys.argv[1] # Pass the month as input
#st_month = str(12) #str(int(month) - 1).zfill(2) # Starting month is one day earlier
#days_in_month = monthrange(2019, int(st_month))[1]
#st_date = pd.to_datetime('2020-%s-%s' % (st_month, str(days_in_month),)) # Set up initial datetime object for start date

domain = sys.argv[2]


# Download turbine coordinates
coords = pd.read_csv('/shared/turbines/%s/windturbines_%s_all_farms.txt' % (domain, domain,), delim_whitespace=True, header = None)
coords.columns = ['lat', 'lon', 'turb_model']

# Download coordinates for Longhorn only
#lh_coords = pd.read_csv('/home/michael.optis@enxco.com/mys3/turbines/longhorn/windturbines_longhorn_only.txt', delim_whitespace=True, header = None)
#lh_coords.columns = ['lat', 'lon', 'turb_model']

# Use example WRF output to get lat lon coordinates
nclist = glob.glob('/mnt/mys3/wrf_runs/%s/all_farms/001/wrfout_d02*01_00:00:00*'
ndata = Dataset(nclist[0])
h = getvar(ndata, "height_agl")
lats, lons = latlon_coords(h)

# Now load the processed WRF data
#dc1 = pk.load(open("/home/michael.optis@enxco.com/mys3/wrf_runs/longhorn/postpro/target_only_%s.p" % month, "rb"))
#dc2 = pk.load(open("/home/michael.optis@enxco.com/mys3/wrf_runs/longhorn/postpro/all_farms_%s.p" % month, "rb"))

# Initialize map to plot wind speed deficits
proj = ccrs.PlateCarree()
#mbounds = [-102, -100.75, 33.4, 34.5]
#t_steps = [n[0] for n in list(dc2.keys())]
#t_max = 10000
#t_max = list(dc2.keys())[-1][0] # Maximum time step of simulation
#print(t_max, type(t_max))

# Initialize key data for power time series comparison
df = pd.DataFrame()
longhorn_extent = [-101.294, -101.189, 34.275, 34.346]
ch = np.where((lats < longhorn_extent[3]) & (lats > longhorn_extent[2]) & (lons < longhorn_extent[1]) & (lons > longhorn_extent[0]))

lat_ran = np.arange(88, 91) # Range of latitudes and longitudes for Longhorn wind farm
lon_ran = np.arange(81, 85) 

print(lats[lat_ran, lon_ran])
print(lons[lat_ran, lon_ran])

levels = np.arange(-5, 5, 0.25) # Contour plotting levels

# Now loop through each 10-minute WRF output and plot
for i,t in enumerate(np.arange(0, t_max, 10)):

    # Grab 80-m wind speed data for the domain
    ws1 = dc1[int(t), 'ws']
    ws2 = dc2[int(t), 'ws']
    
    # define figure
    fig, axes = plt.subplots(1,2, figsize = (15,6))

    ax = axes[0]
    #subplot_kw = dict(projection = proj, extent = mbounds), 
    # Plot coordinates
    ax.plot(coords['lon'], coords['lat'], 'k.', markersize = 1)
    ax.plot(lh_coords['lon'], lh_coords['lat'], 'g.', markersize = 1, zorder = 100)

    # Now make contour plot
    im = ax.contourf(to_np(lons), to_np(lats), to_np(ws1-ws2), cmap='coolwarm', levels = levels)
    
    # Establish consistent colorbar
    cbar1 = fig.colorbar(im, ax=ax, fraction = 0.032, pad=0.02,)
    cbar1.set_label('Wind Speed Deficit (m s$^{-1}$)', fontsize=10)

    # Include stratification and wind speed data in top left corner of map
    th150 = dc1[t, 'th150'].values
    th20 = dc1[t, 'th20'].values
    strat = th150[75,75] - th20[75,75] # Get pot temp. diff at center of domain

    # Make scale for 10km
    delta_x = 0.104 # 10-km distance
    start_x = -100.95
    ax.plot([start_x, start_x + delta_x], [33.5, 33.5], 'k-')
    ax.text(start_x + delta_x/6, 33.51, '10km')

    # Now include stratification and wind speed data
    ax.text(0.025, 0.9, '$\Delta T_{150m-20m}$ = ' + str(np.round(strat,1)) + ' deg C', fontsize = 10, transform = ax.transAxes)
    ax.text(0.025, 0.85, '80-m wind speed = ' + str(np.round(ws1.values[75,75],1)) + ' m/s', fontsize = 10, transform = ax.transAxes)

    ax.set_ylim(mbounds[2], mbounds[3])
    ax.set_xlim(mbounds[0], mbounds[1])
    
    dt = st_date + pd.Timedelta(t, 'T')
    dt_label = str(dt.year)+'_' + str(dt.month).zfill(2) + '_' + str(dt.day).zfill(2) + '_' + str(dt.hour).zfill(2) + '_' + str(dt.minute).zfill(2)
    ax.set_title(dt)

    #################################
    # Now plot power comparison
    #################################
    ax2 = axes[1]
    p1 = dc1[t, 'power']
    p2 = dc2[t, 'power']
    t1 = p1[lat_ran, lon_ran].values
    t2 = p2[lat_ran, lon_ran].values

    df.loc[t, 'longhorn'] = t1.sum()/1e6
    df.loc[t, 'all'] = t2.sum()/1e6
    df.loc[t, 'datetime'] = st_date + pd.Timedelta(t, 'minutes')

    cum_wake_loss = 1 - df['all'].sum()/df['longhorn'].sum()


    ax2.plot(df['datetime'], df['all'], 'C0', label = "All farms present")
    ax2.plot(df['datetime'], df['longhorn'], 'C1', label = 'Just Longhorn present')
    ax2.set_title('Power Production at Longhorn')
    ax2.set_ylabel('Power production (MW)')
    ax2.set_xlabel('Time')
    ax2.set_xlim(st_date, st_date+pd.Timedelta(3, 'days'))
    #end_date = st_date + pd.Timedelta(t_max, 'minutes')
    #marker_dates = [st_date + pd.Timedelta(n, 'minutes') for n in np.arange(0, t_max + 10, t_max/4)]
    #ax2.set_xlim(st_date, end_date)
    #ax2.set_xticks(marker_dates)
    
    ax2.text(0.6, 0.025, 'Cumulative wake loss: ' + str(np.round(cum_wake_loss*100,1)) + '%', transform = ax2.transAxes, fontsize = 10)
    ax2.legend(loc = 'upper right')

    print(dt)
    plt.tight_layout()
    os.system("mkdir ./animations/ws_deficit_map/%s" % month)
    plt.savefig('./animations/ws_deficit_map/%s/%s.jpg' % (month, dt_label, ), dpi = 100)
    plt.close()

