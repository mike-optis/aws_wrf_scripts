#!/bin/bash  

conda activate p3_default

root_dir="/scratch/moptis/wrf_runs/nwpacific/"
run_dir=$root_dir/$wp/$wr/$year/$month

cd $run_dir	   
echo $run_dir

python /projects/oswwra/scripts/python/08_restart_runs.py $run_dir
#sbatch -J $wr_$year_$month ./submit_wrf.sh

