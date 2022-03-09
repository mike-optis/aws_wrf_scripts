#!/bin/bash

#SBATCH --ntasks=20 # One for each month
#SBATCH --time=1:00:00
#SBATCH --job-name=process_wrf_h5
#SBATCH --account=oswwra
#SBATCH --mail-user=andrew.kumler@nrel.gov
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --output=job_output_filename.%j.out  # %j will be replaced with the job ID
#SBATCH --partition=debug


#source activate openoa-env

for wps in WPS1 WPS2 WPS3 WPS4
#for wps in WPS1
do
    for wrf in WRF1 WRF3 WRF5 WRF7
    #for wrf in WRF1
    do
	#python /projects/oswwra/scripts/python/10_process_h5_na2.py ${wps} ${wrf} &
	python /projects/oswwra/scripts/python/10_process_h5_wdir.py ${wps} ${wrf} & 
    done

done


