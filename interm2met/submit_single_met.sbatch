#!/bin/bash
#SBATCH --partition=short
#SBATCH --ntasks=1
#SBATCH --time=3:59:00
#SBATCH --account=boematl # Accounting
#SBATCH --output=ensemble.log.%j

 module purge
 module load conda
 module load netcdf-c/4.6.2/intel-18.0.3-mpi
 module load netcdf-f/4.4.4
 module load hdf5/1.10.4/intel1803-impi
 module load wrf/4.1.2/intel-18.0.3-mpi
 module load gcc/7.3.0
 module load intel-mpi/2018.0.3
 module load comp-intel/2018.0.3



export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nopt/nrel/apps/hdf5/lib:

source activate py37

srun -n 1 python3 2020_02/wps_ensemble.py 
