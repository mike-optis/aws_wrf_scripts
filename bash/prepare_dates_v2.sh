#!/bin/bash

# Let's test out the script for the GFS_MUR dataset and WRF 3.9, and Rutgers namelist. Once working, we can generalize to different datasets, WRF versions, and namelists

# Load modules
module load conda/5.1
source activate reanal3

# Specify start and stop points for number of simulations
num_sim=183 # total is 183
wrf_version="4_0"
namelist="rutgers"

# Define the different reanalysis-sst combinations we will loop through
#declare -a arr=("gfs_nosst" "erai_nosst" "erai_ncep" "gfs_ncep" "gfs_rtg" "erai_rtg") # Start with two for now

#declare -a arr=("gfs_nosst" "gfs_ncep" "gfs_rtg" "erai_nosst" "erai_ncep")

declare -a arr=("gfs_rtg") 

# Loop through each reanalysis-sst combination
for a in "${arr[@]}" 
	do
    
        # Copy over namelist to temp directory
        #cp /projects/rutgers/namelists/input/namelist.input_rutgers_v3_9_v2 /scratch/moptis/rutgers/wrf_3_9/WRFV3/run/namelist.input

	# Specify root directories to store WRF code and WRF output for each 3-day simulation
	wrfout_dir="/scratch/moptis/rutgers/wrfout_full/$wrf_version/$namelist/$a/" # WRF output
	wrf_temp_dir="/scratch/moptis/rutgers/wrf_temp/$wrf_version/$namelist/$a/" # WRF code
	
	echo $wrfout_dir
	echo $wrf_temp_dir
	# Remove directories if they exist already
	
	#rm -r "$wrfout_dir"
	#rm -r "$wrf_temp_dir"

	# Now create directories
	#mkdir "$wrfout_dir"
	#mkdir "$wrf_temp_dir"

	# Link the relevant met files into the temporary WRF run directory (first removing any that are there
	#rm /scratch/moptis/rutgers/wrf_3_9/WRFV3/run/met_em*
	#ln -sf /scratch/moptis/rutgers/metgrid_files/v3_9/$a/met_em* /scratch/moptis/rutgers/wrf_3_9/WRFV3/run/
	
	i=1 # Start counter
	# Now loop through the 182 required 3-day simulations, temporarily store WRF code, and run WRF
	for ((k=$i; k<=$num_sim; k++))
		do
		echo $k
	
		# Create 3-day run directory using integer numbers
		rm -r "$wrfout_dir$k"
		rm -r "$wrf_temp_dir$k"
		mkdir "$wrfout_dir$k" 
		mkdir "$wrf_temp_dir$k" 
	
		# Go to temp WRF directory and link in WRF files
		cd "$wrf_temp_dir$k" 
		#ln -s /scratch/moptis/rutgers/wrf/$wrf_version/WRF/run/* ./
		ln -s /projects/rutgers/WRF$wrf_version/run/* ./
		ln -sf /projects/rutgers/metgrid_files/v$wrf_version/$a/met_em* .
		# Copy over namelist directly (do we need to?)
		rm ./namelist.input
		
		#cp "/projects/rutgers/namelists/input/namelist.input_$namelist" ./namelist.input
		cp /projects/rutgers/namelists/input/namelist.input_rutgers_high_vert_res ./namelist.input

		cp /projects/rutgers/custom_files/tslist_rutgers ./tslist
                cp /projects/rutgers/custom_files/myoutfields.txt . 

		# Copy submit script to temp WRF location
		cp /projects/rutgers/scripts/submit_WRF.sh .
	        
		# Update namelist for next simulation
                python /projects/rutgers/scripts/update_namelist_v2.py $k $a $wrf_version $namelist

		# Launch simulation from temp WRF directory
		qsub submit_WRF.sh
	done
done
