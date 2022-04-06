#!/bin/bash -l


pip install cdsapi
pip install numpy

#for y in {2019..2020}
for y in 2020
do

#for i in {01..12}
for i in 06
do
   python ./GetERA5-pl.py $y $i
   python ./GetERA5-sl.py $y $i
   echo $i
done
done


