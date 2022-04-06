#!/bin/bash

domain="bobcat"
type="target_only"
#for n in 001
for n in {001..179}
do
  echo $n
  export n
  export type
  sbatch ./04_submit_wrf.sbatch
done
