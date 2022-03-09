#!/bin/bash -l


#conda activate era5
#pip install cdsapi

for y in {2018..2020}
#for y in 2018
do

for m in {01..12}
do
   
   cd /mys3bucket/era5_data/${y}/${m} 
   echo $y
   echo $m
   ls -l | tail -1
   #echo $i
done
done


