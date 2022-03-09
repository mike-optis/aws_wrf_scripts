#!/bin/bash

source activate p3_default

root_dir='/scratch/moptis/wrf_runs/nwpacific/'
wps='WPS1'
start_month=1
end_month=12
domain='nwpacific'
reanalysis='era5'

#for y in 2020
for y in {2012..2019}
do
    echo $y
    python /projects/oswwra/scripts/python/04_namelist.input.py $root_dir $wps $y $start_month $end_month $domain $reanalysis
done
