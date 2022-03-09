#!/bin/bash  

# This script swaps OSTIA ddata in WPS1 with MUR data
# via Pat's scripts. Data is saved into WPS2 met_data folder
# (same applies for WPS3 to WPS4)

root_dir='/scratch/moptis/wrf_runs/prod-midatlantic/'
echo ${root_dir}
first_wps='WPS1/' # Where we'll copy from
new_wps='WPS2/' # Where data will go

met_folder='met_data/'

mkdir -p ${new_wps}/met_data # Make new wps met data directory

#start_date='2019_09' # First met folder
#end_date='2020_08' # Second met folder

# Create new directories
#cd $HOME

first_wps_dir=${root_dir}${first_wps}${met_folder}
new_wps_dir=${root_dir}${new_wps}${met_folder}

#echo ${first_wps_dir}
#echo ${new_wps_dir}

cd ${first_wps_dir}

for m in 2* # Loop through all month folders and create folders in new wps root folder
do
    cd ${root_dir}
    #echo $m
    #echo ${new_wps_dir}/${m}
    mkdir -p ${new_wps_dir}/${m}
done

# Now loop through each new directory, call Pat's script,
# and produce new met_em files with MUR SST data

cd ${new_wps_dir}
#echo ${new_wps_dir}

source activate p3_default

for m in 2* # Loop through monthly folders
do
    ref_folder=${first_wps_dir}/${m}/
    target_folder=${new_wps_dir}/${m}/
    python /projects/oswwra/scripts/sst/ghrsst/OverwriteSST.py ${ref_folder} ${target_folder}
done 
