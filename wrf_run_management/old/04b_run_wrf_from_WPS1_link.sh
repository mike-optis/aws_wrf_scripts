#!/bin/bash  

root_dir="/scratch/moptis/wrf_runs/prod-midatlantic/"

cd $root_dir

declare -a months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")


declare -a wps=("WPS1")   
declare -a wrf=("WRF2" "WRF3" "WRF4")

for wp in WPS1
#for wp in "${wps[@]}"; # Loop through WPS setups                                                                                                                                                                  
do
   for wr in WRF1
   #for wr in "${wrf[@]}"
   do
       for y in 2020
       do
	   #for m in "${months[@]}"
	   for m in {07..08}
           do
       
	   run_dir=$root_dir/$wp/$wr/$y/$m/
	   echo $run_dir
	   ln -sf  /nopt/nrel/apps/wrf/WRF-4.2.1/bin/wrf.exe.pn-hb $run_dir/wrf.exe
    
	   #ln -sf $root_dir/$wp/WRF1/$y/$m/wrf*d01 $run_dir
           #ln -sf $root_dir/$wp/WRF1/$y/$m/wrf*d02 $run_dir

	   cp /projects/oswwra/meta_data/submit_wrf.sh.midatlantic $run_dir/submit_wrf.sh
	   #cp /projects/oswwra/meta_data/myoutfields.txt $run_dir
	   #rm $run_dir/wrf.exe
	   #cp /projects/oswwra/alex_scripts/WRFV3/run/wrf.exe $run_dir
	   cd $run_dir
	   #sbatch ./submit_wrf.sh
	   sbatch -J ${wr}_${y}_$m ./submit_wrf.sh

	   cd $root_dir
	   done
	done
    done
done
