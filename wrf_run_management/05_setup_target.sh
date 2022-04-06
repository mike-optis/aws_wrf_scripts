
#!/bin/bash

domain='bobcat'

for d in {001..179}
do
    echo $d
    cd /shared/target_only/$d
    ln -sf /shared/all_farms/$d/wrfb* .
    ln -sf /shared/all_farms/$d/wrfi* .
    cp /shared/all_farms/$d/namelist.input .
done





