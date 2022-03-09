#!/bin/bash

#SBATCH --job-name=wrf					        # Job-name=WRFGr_64
#SBATCH --ntasks=16						# Number of MPI ranks
#SBATCH --exclusive

#export I_MPI_OFI_LIBRARY_INTERNAL=0
spack load intel-oneapi-mpi
spack load wrf
module load libfabric-aws
set -x
ulimit -s unlimited
ulimit -a

mpirun -np 16 ./wrf.exe 
#echo $n
