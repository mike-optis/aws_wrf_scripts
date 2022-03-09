#!/bin/bash
#SBATCH --ntasks=1                # Request 100 CPU cores
#SBATCH --time=00:05:00             # Job should run for up to 6 hours
#SBATCH --account=boematl # Accounting
#SBATCH --mail-user=mike.optis@nrel.gov 
#SBATCH --output=job_output_filename.%j.out  # %j will be replaced with the job ID 
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=mike.optis@nrel.gov  
#SBATCH --partition=short

sleep 100
echo 'test'
