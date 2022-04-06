#!/bin/bash

domain='bobcat'

for n in {001..179}
#for n in 179
do
  
  echo $n

  for f in ./all_farms/$n/wrfout*
  do
    aws s3 mv $f s3://nwpm/wrf_runs/$domain/all_farms/$n/
  done
  
  for f in ./target_only/$n/wrfout*
  do
    aws s3 mv $f s3://nwpm/wrf_runs/$domain/target_only/$n/
  done
  
  for f in ./all_farms/$n/wrfrst*
  do
    aws s3 mv $f s3://nwpm/wrf_runs/$domain/all_farms/$n/
  done

  for f in ./target_only/$n/wrfrst*
  do
    aws s3 mv $f s3://nwpm/wrf_runs/$domain/target_only/$n/
  done
done
