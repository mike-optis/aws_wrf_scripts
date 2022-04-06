#!/bin/bash

#conda activate postpro

domain="rockfalls"
type="target_only"

root_dir="/shared/${type}/"
#s3_dir="/mnt/mys3/wrf_runs/${domain}/${type}/"
s3_dir="/shared/${type}/"

new_ts='15' # New time step to use

#./02_import_namelist.sh

#for n in {001..179}
for n in {131..179}
do
        run_dir=${root_dir}/$n/
        save_dir=${s3_dir}/$n/
        echo $run_dir
        echo $save_dir
        #ln -sf ${save_dir}/${y}_${m}/wrfrst* $run_dir
        
        python /shared/scripts/python/08_restart_runs.py $run_dir $save_dir $new_ts
        
        #export n
        #sbatch ./03_submit_wrf.sbatch
done
wait

