#!/bin/bash 

cd /scratch/moptis/wrf_runs/nwpacific

for year in {2000..2019}
do
    export year
    for month in {01..12}
    #for month in 11
    do
	export month
	for wp in WPS1
	do
	    export wp
	    for wr in WRF1
	    do
		export wr

		squeue -u moptis -t R,PD -n ${wr}_${year}_${month} | grep moptis ||  ./05a_restart_run.sh 
	    done
	done
    done
done
