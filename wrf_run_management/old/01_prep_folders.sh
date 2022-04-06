#!/bin/bash

# Load namelists
domain='longhorn'
python /mnt/efs/fs1/scripts/python/04_namelist.input.py $domain

# Copy over WRF code
for d in {001..179}
do
    cp /home/centos/NESTED2/run/*_DATA ./$d
    cp /home/centos/NESTED2/run/*_DBL ./$d
    cp /home/centos/NESTED2/run/*_rain ./$d
    cp /home/centos/NESTED2/run/*TBL ./$d
    cp /home/centos/NESTED2/run/*formatted ./$d
    cp /home/centos/NESTED2/main/real.exe ./$d/real.exe
    cp /home/centos/NESTED2/main/real.exe ./$d/wrf.exe

    #cp /mnt/efs/fs1/turbines/${domain}/
done
