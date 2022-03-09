#!/bin/bash -l


#conda activate era5
#pip install cdsapi


for y in {2018..2020}
#for y in 2020
do

for m in {01..12}
do
   
   cd /mys3bucket/era5_data/interm/${y}/${m} 
   echo $y
   echo $m
   ls -lrt ERA5_P* | tail -1
   #echo $i
done
done


