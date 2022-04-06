#!/bin/bash  

root_dir="/scratch/moptis/wrf_runs/prod-midatlantic/"

for wp in WPS1
do
   for wr in WRF2 WRF3 WRF4
   do    
       for m in {01..08}
       do
	   for y in 2020
	   do
	       run_dir=$root_dir/$wp/$wr/$y/$m/
	       parent_dir=$root_dir/$wp/WRF1/$y/$m
	       
	       echo $run_dir
               
	       # Link boundary forcing files
	       ln -sf $parent_dir/wrfb* $run_dir
	       ln -sf $parent_dir/wrfl* $run_dir
	       ln -sf $parent_dir/wrfi* $run_dir 
	       ln -sf $parent_dir/wrff* $run_dir
	       done
	   done
     done
done
