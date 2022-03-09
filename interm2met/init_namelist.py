#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:32:14 2019

@author: Alex Rybchuk

Initialize namelist share and geogrid sections
"""

import os

def set_share(start_date_str, end_date_str, interval_seconds, max_dom):
    ### Read in the template
    template_file = "namelist.wps.template"
    f = open(template_file, "rt")
    filedata = f.read()
    f.close()


    ### Populate template
    newdata = filedata.replace('$START_DATE', start_date_str)
    newdata = newdata.replace('$END_DATE', end_date_str)
    newdata = newdata.replace('$INTERVAL_SECONDS', str(interval_seconds))
    newdata = newdata.replace('$MAX_DOM', str(max_dom))

    ### Output template
    out_file = "namelist.wps.out1"
    f = open(out_file, "w")
    f.write(newdata)
    f.close()

def set_geogrid(ref_lat, ref_lon, stand_lon,
                d1_ewe, d2_ewe, d3_ewe, d1_esn, d2_esn, d3_esn,
                d2_i, d3_i, d2_j, d3_j):
    ### Read in the template
    template_file = "namelist.wps.out1"
    f = open(template_file, "rt")
    filedata = f.read()
    f.close()

    ### Populate template
    # Domain location
    newdata = filedata.replace('$D1_I', str(1))
    newdata = newdata.replace('$D2_I', str(d2_i))
    newdata = newdata.replace('$D3_I', str(d3_i))
    newdata = newdata.replace('$D1_J', str(1))
    newdata = newdata.replace('$D2_J', str(d2_j))
    newdata = newdata.replace('$D3_J', str(d3_j))

    # Domain size
    newdata = newdata.replace('$D1_EWE', str(d1_ewe))
    newdata = newdata.replace('$D2_EWE', str(d2_ewe))
    newdata = newdata.replace('$D3_EWE', str(d3_ewe))
    newdata = newdata.replace('$D1_ESN', str(d1_esn))
    newdata = newdata.replace('$D2_ESN', str(d2_esn))
    newdata = newdata.replace('$D3_ESN', str(d3_esn))

    # Map projection paramerers
    newdata = newdata.replace('$REF_LAT', '{:3.2f}'.format(ref_lat))
    newdata = newdata.replace('$REF_LON', '{:3.2f}'.format(ref_lon))
    newdata = newdata.replace('$STAND_LON', '{:3.2f}'.format(stand_lon))

    ### Output template
    out_file = "namelist.wps"
    f = open(out_file, "w")
    f.write(newdata)
    f.close()
    os.system('chmod 777 namelist.wps')
    
    ### Delete old file
    os.system("rm namelist.wps.out1")
