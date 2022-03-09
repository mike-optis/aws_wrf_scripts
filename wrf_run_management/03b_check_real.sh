#!/bin/bash  


declare -a months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")
#declare -a months=("01")

declare -a wps=("WPS1" "WPS2" "WPS3" "WPS4")

#for wp in "${wps[@]}"; # Loop through WPS setups                                                                                                        
for wp in WPS1                                         
do
   #for wr in WRF1 WRF3 WRF5 WRF7
   for wr in WRF1
   do
       for y in {2000..2007}
       #for y in {2000..2019}
       do
	   for m in "${months[@]}"
	   do
       	   
	       run_dir=./$wp/$wr/$y/$m/

	       echo $run_dir
	       tail -1 $run_dir/rsl.out.0000
	       #ls -l $run_dir/rsl.out.0000
	       #ls -l $run_dir/custom_wrfout_d02* | tail
	   done
       done
    done
done
