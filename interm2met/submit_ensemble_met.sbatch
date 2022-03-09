#!/bin/bash
#SBATCH --ntasks=36
#SBATCH --time=04:00:00
#SBATCH --account=oswwra # Accounting
#SBATCH --output=ensemble.log.%j
#SBATCH --partition=short

 module purge
 module load conda
 #module load netcdf-c/4.6.2/intel-18.0.3-mpi
 #module load netcdf-f/4.4.4
 #module load hdf5/1.10.4/intel1803-impi
 #module load wrf/4.1.2/intel-18.0.3-mpi
 #module load gcc/7.3.0
 #module load intel-mpi/2018.0.3
 #module load comp-intel/2018.0.3
 module load wrf/4.1.3 netcdf-c/4.6.2 netcdf-f/4.4.4




#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nopt/nrel/apps/hdf5/lib:

source activate /home/moptis/.conda-envs/p3_default

srun -n 1 python3 ${year}_${month}/wps_ensemble.py prod-midatlantic

cd ./${year}_${month}

#srun -n 1 ./geogrid.exe
#srun -n 1 ./metgrid.exe
#mpirun -4 ./metgrid
