#!/bin/bash

root_dir="/scratch/moptis/wrf_runs/nwpacific/"

cd $root_dir

declare -a months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")
#declare -a wps=("WPS2" "WPS3" "WPS4")
declare -a wps=("WPS1")
declare -a wrf=("WRF2" "WRF3" "WRF4") # Just need real.exe data for first WRF setup

for wp in "${wps[@]}"; # Loop through WPS setups
do
    #for wr in "${wrf[@]}" # Loop through WRF setups
    for wr in WRF1
    do
	for y in {2012..2019}
	do
	    for m in {01..12}
	    #for m in "${months[@]}"
	    do
	    d=$wp/$wr/$y/$m
	    echo $d

	    mkdir -p $d
	    
	    #rm -r $wp/$wr
	    rsync -a /nopt/nrel/apps/wrf/WRF-4.2.1/run/*_DATA ./$d                                                                                                                                                  
	    rsync -a /nopt/nrel/apps/wrf/WRF-4.2.1/run/*_DBL ./$d                                                                                                                                                   
	    rsync -a /nopt/nrel/apps/wrf/WRF-4.2.1/run/*_rain ./$d                                                                                                                                                  
	    rsync -a /nopt/nrel/apps/wrf/WRF-4.2.1/run/*TBL ./$d                                                                                                                                                    
	    rsync -a /nopt/nrel/apps/wrf/WRF-4.2.1/run/*formatted ./$d                                                                                                                                              
	    ln -sf  /nopt/nrel/apps/wrf/WRF-4.2.1/bin/real.exe.pn-hb ./$d/real.exe                                                                                                                                  
	    cp /projects/oswwra/meta_data/myoutfields.txt ./$d
            done
	done
    done
done
