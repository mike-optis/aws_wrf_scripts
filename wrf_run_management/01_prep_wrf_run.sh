
#!/bin/bash

domain='bobcat'

for d in {001..179}
do
for t in target_only all_farms
do
    echo $d
    mkdir -p ./$t/$d

    ln -sf /shared/turbines/$domain/wind-t* ./$t/$d

    ln -sf $WRF_ROOT/*DATA ./$t/$d
    ln -sf $WRF_ROOT/*DBL ./$t/$d
    ln -sf $WRF_ROOT/*rain ./$t/$d
    ln -sf $WRF_ROOT/*TBL ./$t/$d
    ln -sf $WRF_ROOT/*formatted ./$t/$d
    ln -sf $WRF_ROOT/real.exe ./$t/$d
    ln -sf $WRF_ROOT/wrf.exe ./$t/$d

done
ln -sf /shared/turbines/$domain/windturbines_${domain}_only.txt ./target_only/$d/windturbines.txt
ln -sf /shared/turbines/$domain/windturbines_${domain}_all_farms.txt ./all_farms/$d/windturbines.txt
done





