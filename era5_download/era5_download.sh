#!/bin/bash -l


conda activate era5
#pip install cdsapi

#for y in {2019..2020}
for y in 2019
do

#for i in {01..12}
for i in 4
do
   #python ./GetERA5-pl.py $y $i
   python ./GetERA5-sl.py $y $i
   echo $i
done
done


