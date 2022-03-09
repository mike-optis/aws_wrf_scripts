#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:14:57 2019

@author: orybchuk

This script executes geogrid
"""

import os

def run_geogrid():
    ### Link geogrid
    os.system("ln -sf $WPS_ROOT/geogrid/GEOGRID.TBL .")
    os.system("ln -sf $WPS_ROOT/geogrid.exe .")
    ### Run geogrid
    os.system("./geogrid.exe")
    
    ### Print the status of the completed run
    #log_file = open("geogrid.log", "r")
    #last_line = log_file.readlines()[-1]
    #print(last_line)
