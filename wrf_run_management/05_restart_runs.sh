#!/bin/bash  

source activate p3_default

root_dir="/projects/oswwra/tap/prod-offshoreCA/"

cd $root_dir

declare -a months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")
declare -a wps=("WPS1" "WPS2" "WPS3" "WPS4")
#declare -a wps=("WPS4")
declare -a wrf=("WRF1" "WRF3" "WRF5" "WRF7")
#declare -a wrf=("WRF1")

#for wp in "${wps[@]}"; # Loop through WPS setups                                                                                                                   
for wp in WPS1                                              
do
   #for wr in "${wrf[@]}"
   for wr in WRF6
   do
       for y in 2017
       #for y in {2000..2018}
       do
	   for m in 07
	   #for m in "${months[@]}"
	   do
	   
	       run_dir=$root_dir/$wp/$wr/$y/$m/
	   
	       echo $run_dir
	       #cp /projects/oswwra/meta_data/submit_wrf_1day.sh $run_dir/submit_wrf.sh
	       python /projects/oswwra/scripts/python/08_restart_runs.py $run_dir
       
	   done
       done
    done
done
