#!/bin/bash

#SBATCH --ntasks=20 # One for each month
#SBATCH --time=01:00:00
#SBATCH --job-name=process_wrf_h5
#SBATCH --account=oswwra
#SBATCH --mail-user=mike.optis@nrel.gov
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --output=job_output_filename.%j.out  # %j will be replaced with the job ID
#SBATCH --partition=debug

source activate h5py

for wps in 1 2 3 4
do
    for wrf in 1 3 5 7
    do
	python /projects/oswwra/scripts/python/10_process_h5_na2.py ${wps} ${wrf} &
    done

done


