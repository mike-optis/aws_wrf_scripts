#!/bin/bash

type="all_farms"
export $type
for n in {080..090}
do
  echo $n
  export n
  sbatch ./03_submit_real.sbatch
done
