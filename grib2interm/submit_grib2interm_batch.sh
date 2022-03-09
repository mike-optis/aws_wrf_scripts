#!/bin/bash

# MAKE SURE THE NUMBER OF SUBMISSIONS MATCHES ntasks ABOVE
#srun -n 1 python grib_to_interm.py 2020-09-01 2020-10-01 &
#srun -n 1 python grib_to_interm.py 2020-10-01 2020-11-01 &
#srun -n 1 python grib_to_interm.py 2020-11-01 2020-12-01 &
#python grib_to_interm.py 2019-12-31 2020-01-01 &
#python grib_to_interm.py 2020-02-01 2020-03-01 &
#python grib_to_interm.py 2020-03-01 2020-04-01 &
#python grib_to_interm.py 2020-04-01 2020-05-01 &
#python grib_to_interm.py 2020-05-01 2020-06-01 &



#python grib_to_interm_old.py 2019-01-01 2019-02-01
#python grib_to_interm_old.py 2019-02-01 2019-03-01
#python grib_to_interm_old.py 2019-03-01 2019-04-01
#python grib_to_interm_old.py 2019-04-01 2019-05-01
#python grib_to_interm_old.py 2019-05-01 2019-06-01
#python grib_to_interm_old.py 2019-06-01 2019-07-01
#python grib_to_interm_old.py 2019-07-01 2019-08-01
#python grib_to_interm_old.py 2019-08-01 2019-09-01
#python grib_to_interm_old.py 2019-09-01 2019-10-01
#python grib_to_interm_old.py 2019-10-01 2019-11-01
#python grib_to_interm_old.py 2019-11-01 2019-12-01
#python grib_to_interm_old.py 2019-12-01 2020-01-01


#mpirun -np 1 python grib_to_interm_old.py 2020-05-01 2020-06-01

#mpirun -np 1 python grib_to_interm_old.py 2018-01-01 2018-02-01 &
#mpirun -np 1 python grib_to_interm_old.py 2018-02-01 2018-03-01 &
#mpirun -np 1 python grib_to_interm_old.py 2018-03-01 2018-04-01 & 
#mpirun -np 1 python grib_to_interm_old.py 2019-04-01 2019-05-01 &
#mpirun -np 1 python grib_to_interm_old.py 2019-05-01 2019-06-01 &
#mpirun -np 1 python grib_to_interm_old.py 2018-06-01 2018-07-01 &
#mpirun -np 1 python grib_to_interm_old.py 2019-07-01 2019-08-01 &
#mpirun -np 1 python grib_to_interm_old.py 2019-08-01 2019-09-01 &
#mpirun -np 1 python grib_to_interm_old.py 2018-09-01 2018-10-01 & 
#mpirun -np 1 python grib_to_interm_old.py 2018-10-01 2018-11-01 &
#mpirun -np 1 python grib_to_interm_old.py 2018-11-01 2018-12-01 &
mpirun -np 1 python grib_to_interm_old.py 2018-12-01 2019-01-01 &

#mpirun -np 1 python grib_to_interm_old.py 2021-01-01 2021-01-01
#python grib_to_interm_old.py 2018-01-01 2018-02-01
#python grib_to_interm_old.py 2018-02-01 2018-03-01
#python grib_to_interm_old.py 2018-03-01 2018-04-01
#python grib_to_interm_old.py 2018-04-01 2018-05-01
#python grib_to_interm_old.py 2018-05-01 2018-06-01
#python grib_to_interm_old.py 2018-06-01 2018-07-01
#python grib_to_interm_old.py 2018-07-01 2018-08-01
#python grib_to_interm_old.py 2018-08-01 2018-09-01
#python grib_to_interm_old.py 2018-09-01 2018-10-01

#done
#python grib_to_interm.py 2020-07-01 2020-08-01 &
#python grib_to_interm.py 2020-08-01 2020-09-01 &
#python grib_to_interm.py 2020-09-01 2020-10-01 &
#python grib_to_interm.py 2020-10-01 2020-11-01 &
#python grib_to_interm.py 2020-11-01 2020-12-01 &
#python grib_to_interm.py 2020-12-31 2021-01-01 &
