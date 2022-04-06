#!/bin/bash

#SBATCH --job-name=WRF
#SBATCH --output=conus-%j.out
#SBATCH --ntasks=16
#SBATCH --exclusive

#export I_MPI_OFI_LIBRARY_INTERNAL=0
spack load intel-oneapi-mpi
spack load wrf
module load libfabric-aws
set -x
ulimit -s unlimited
ulimit -a

#export OMP_NUM_THREADS=6
#export FI_PROVIDER=efa
#export I_MPI_FABRICS=ofi
#export I_MPI_OFI_PROVIDER=efa
#export I_MPI_PIN_DOMAIN=omp
#export KMP_AFFINITY=compact
#export I_MPI_DEBUG=4

cd /shared/$type/$n/
mpirun -np 16 ./wrf.exe
