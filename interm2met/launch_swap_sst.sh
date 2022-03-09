#!/bin/bash

for year in 2008
do
    export year
    sbatch ./submit_sst_swap.sh
done
