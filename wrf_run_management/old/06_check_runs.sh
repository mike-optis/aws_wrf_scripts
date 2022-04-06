#!/bin/bash  

root_dir="./"

cd $root_dir

declare -a months=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11" "12")
#declare -a wps=("WPS1" "WPS2" "WPS3" "WPS4")
declare -a wps=("WPS1")
declare -a wrf=("WRF1" "WRF2" "WRF3" "WRF4")
#declare -a wrf=("WRF1" "WRF3" "WRF5" "WRF7")
#declare -a wrf=("WRF1")

#for wp in "${wps[@]}"; # Loop through WPS setups                                                                                                                            
for wp in WPS1                                      
do
    #for wr in "${wrf[@]}"
    for wr in WRF1   
    do
       for y in {2000..2019}
       do
       echo $y
       
          for m in "${months[@]}"
	  #for m in 12
          do
	   
	      run_dir=$root_dir/$wp/$wr/$y/$m/
	   
#	      echo $run_dir
	      tail -1 $run_dir/rsl.out.0000
	      #ls -lrt $run_dir/rsl.out.0000
	  done
       done
    done
done
