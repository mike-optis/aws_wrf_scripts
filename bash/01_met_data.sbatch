#!/bin/bash
#
#SBATCH --job-name=run_met					# Job-name=WRFGr_64
#SBATCH --output=/mnt/efs/fs1/scripts/bash/out_met.log	# Standard output			
#SBATCH --ntasks=12						# Number of MPI ranks

cd /home/centos/WRF-4.3/test/case2
mpirun /home/centos/WRF-4.3/test/case2/wrf.exe 
