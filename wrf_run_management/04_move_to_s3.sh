#!/bin/bash

for n in {001..179}
do
  echo $n
  mv /mnt/efs/fs1/wrf_runs/longhorn/all_farms/$n/wrfout* /shared/mys3/wrf_runs/longhorn/all_farms/$n/
  mv /mnt/efs/fs1/wrf_runs/longhorn/all_farms/$n/wrfrst* /shared/mys3/wrf_runs/longhorn/all_farms/$n/
  mv /mnt/efs/fs1/wrf_runs/longhorn/target_only/$n/wrfout* /shared/mys3/wrf_runs/longhorn/target_only/$n/
  mv /mnt/efs/fs1/wrf_runs/longhorn/target_only/$n/wrfrst* /shared/mys3/wrf_runs/longhorn/target_only/$n/
done
