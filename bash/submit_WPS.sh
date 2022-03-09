#!/bin/bash

#SBATCH --ntasks=12 # One for each month
#SBATCH --time=24:00:00
#SBATCH --job-name=WPS_SETUP
#SBATCH --account=boematl
#SBATCH --mail-user=mike.optis@nrel.gov
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --output=job_output_filename.%j.out  # %j will be replaced with the job ID

# Load the modules that we need
module purge
module load intel-mpi/2018.0.3
module load netcdf-f/4.4.4
module load netcdf-c/4.6.2/intel-18.0.3-mpi
module load hdf5/1.10.4/intel1803-impi
export NETCDF=$NETCDF_FORTRAN
export HDF5=$HDF5_ROOT_DIR
export LD_LIBRARY_PATH="/home/moptis/temp/wrf/build_wrf/LIBRARIES/grib2/lib:$LD_LIBRARY_PATH"

# Load python env. we need
module load conda
conda activate p3_default 

# Get region info to namelist file
region='ca_offshore'

# Create new WPS file for the given region
python /projects/oswwra/scripts/python/01_set_regions.py $region

# Now we need to loop through each month, edit the new regional WPS file to adjust the dates
# resave into separate months

