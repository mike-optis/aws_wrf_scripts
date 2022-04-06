
#!/bin/bash

domain='bobcat'
t='target_only'
#t='all_farms'

for d in {001..179}
#for d in 031 035 092 179
do
    echo $d
    tail -1 ./$t/$d/rsl.out.0000
    #ls -lrt ./$t/$d/rsl.out.0000 | tail -1
done





