#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:34:48 2020

@author: Alex Rybchuk, alex.rybchuk@gmail.com

Convert ERA5 .grib files to Intermediate files
    First convert surface data
    Second convert pressure data
This script only works on a single month of data,
    so use shell scripts to submit this file 
    many times for many months in parallel
"""

from tempfile import mkstemp
from shutil import move
import os
import sys
from datetime import datetime, timedelta

def grib2interm(sdate, edate, gribpath, intermpath, scriptpath):
    '''
    Converts ERA5 .grib files to Intermediate files
    '''
    ### ~~~~~~~~~~~~~~ PROCESS SURFACE FILES ~~~~~~~~~~~~~~~~~~~     
    ## Link .grib files
    my_date = sdate
    outpath = intermpath+str(sdate.year)+"/"+str(sdate.month).zfill(2)+"/"
    while my_date <= edate:
        # Date
        year = my_date.year
        month = my_date.month
        day = my_date.day
        
        # Directory management
        inpath = gribpath+str(year)+"/"+str(month).zfill(2)+"/*surface*"+ \
                  str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)
#        outpath = intermpath+str(year)+"/"+str(month).zfill(2)+"/"
        if not os.path.exists(outpath):
            os.makedirs(outpath)
                    
        # Link file
        os.system("ln -sf "+inpath+"* "+outpath+".")

        my_date += timedelta(days=1)
    print("Linked to ERA5 surface .grib files!")

        
    ## Copy over namelist and modify
#    os.system("cp -pa "+scriptpath+"namelist.wps.grib2interm "+
#              outpath+"namelist.wps")
    
    with open(scriptpath+"namelist.wps.grib2interm") as old_file:
        filedata = old_file.read()
        filedata = filedata.replace('STARTDATE', 

            for line in old_file:
                if ((' prefix' not in line) and
                    ('start_date' not in line) and
                    ('end_date' not in line)):
                        new_file.write(line)
                elif ' prefix' in line:
                    new_file.write(" prefix = 'ERA5_SURF',\n")
                elif 'start_date' in line:
                    sdate_fmt = sdate.strftime("'%Y-%m-%d_%H:%M:%S',\n")
                    new_file.write(" start_date = "+sdate_fmt)
                elif 'end_date' in line:
                    edate_fmt = edate.strftime("'%Y-%m-%d_%H:%M:%S',\n")
                    new_file.write(" end_date = "+edate_fmt)
    # Remove original file
    os.remove(outpath+'namelist.wps')
    # Move new file
    move(abs_path, outpath+'namelist.wps')
    print('%s/namelist.wps' % outpath)
    #os.system('chmod 777 %s/namelist.wps' % outpath)
    #chmod 777 outpath+'namelist.wps'
    print("Prepared namelist!")
    
    ## Change directory + set up Vtable, link_grib.sh, and ungrib.exe
    os.chdir(outpath)


    os.system("ln -sf /home/centos/PREPRO/WPS/ungrib/Variable_Tables/Vtable.ERA-interim.pl Vtable")
    os.system("cp /home/centos/PREPRO/WPS/link_grib.csh .")
    os.system("ln -sf /home/centos/PREPRO/WPS/ungrib.exe .")
    
    ## Run link_grib.sh and ungrib.exe
    print("Linking surface .grib files and ungribbing...")
    os.system("./link_grib.csh *.grib")
    os.system("./ungrib.exe")
    print("    .grib files linked and ungribbed!")

    ## Remove unnecessary data
    #os.system("rm ERA5*")
    os.system("rm GRIBFILE.*")
    
    ### ~~~~~~~~~~~~~~ PROCESS PRESSURE FILES ~~~~~~~~~~~~~~~~~~~     
    ## Link .grib files
    my_date = sdate
    while my_date <= edate:
        # Date
        year = my_date.year
        month = my_date.month
        day = my_date.day
        
        # Directory management
        inpath = gribpath+str(year)+"/"+str(month).zfill(2)+"/*pressure*"+ \
                  str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)
                    
        # Link file
        os.system("ln -sf "+inpath+"* .")

        my_date += timedelta(days=1)
    
    ### Namelist modifications
    fh, abs_path = mkstemp()
    print(abs_path)
    with os.fdopen(fh,'w') as new_file:
        with open('namelist.wps') as old_file:
            for line in old_file:
                if 'prefix' not in line:
                    new_file.write(line)
                else:
                    new_file.write(" prefix = 'ERA5_PRES',\n")
    # Remove original file
    os.remove('namelist.wps')
    # Move new file
    move(abs_path, 'namelist.wps')
    
    ## Run link_grib.sh and ungrib.exe
    print("Linking pressure .grib files and ungribbing...")
    os.system("./link_grib.csh *.grib")
    os.system("./ungrib.exe")
    print("    .grib files linked and ungribbed!")
    
    ## Remove unnecessary data
    #os.system("rm ERA5*")
    os.system("rm GRIBFILE.*")
    

def main():
    pass

    convert=True

    # Read in start and end date for download
    sdate=datetime.strptime(sys.argv[1],"%Y-%m-%d")
    edate=datetime.strptime(sys.argv[2],"%Y-%m-%d")

    # File locations
    gribpath="/mys3bucket/era5_data/"
    intermpath="/mys3bucket/era5_data/interm/" 
    scriptpath="/mnt/efs/fs1/scripts/grib2interm/"

    if convert:
        grib2interm(sdate, edate, gribpath, intermpath, scriptpath)
    print("All Done!")




if __name__ == '__main__':
  main()
