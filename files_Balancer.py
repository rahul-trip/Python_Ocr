#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:33:54 2019

Read the names of .jpg files in the directory and create a sep file for each
number present in the name of the file

inputdir.split(os.sep)[-2]
os.sep.join(inputdir.split(os.sep)[:-1])


@author: rahul
"""

mode = "Development"

#Importing Libraries
import os
import pandas as pd
from pathlib import Path
import logging
import copy

def logger(msg, path, level, x):
    """ function responsible for logging
    """
    #logging.basicConfig(level=20, filename = x)
    
    if level == "DEBUG":
        logging.debug(msg+" --> "+str(path))
    elif level == "INFO":
        logging.info(msg+" --> "+str(path))
    else:
        print("Wrong LOG Level provided!!!")


def recursefunct(inputdir):
    
    content = os.listdir(inputdir)
    for dirctry in content:
        if "complete" in dirctry.lower():
            continue
        if not ".jpg" in dirctry:
            #logger("cant find jpg file here", os.path.join(inputdir, dirctry), "INFO")
            if os.path.isfile(os.path.join(inputdir, dirctry)):
                logger("found a file at: ", os.path.join(inputdir, dirctry), "DEBUG", "log.txt")
            elif os.path.isdir(os.path.join(inputdir, dirctry)):
                logger("It is a directory: ", os.path.join(inputdir, dirctry), "DEBUG", "log.txt")
                recursefunct(os.path.join(inputdir, dirctry))
            else:
                logger("Wrong address !! continued at ", inputdir, "DEBUG", "log.txt")
        elif ".jpg" in dirctry:
            jpgdir_list.append(inputdir)
            logger("Found JPG's here MARK this address!!!", inputdir, "INFO", "log.txt")
            return

def create_file_list(jpgdir_list):
    for jpgdirindx in range(len(jpgdir_list)):
        jpgdir_list[jpgdirindx] = "/".join(jpgdir_list[jpgdirindx].split("/")[:-1])
        logger("found", jpgdir_list[jpgdirindx], "INFO", "log2.txt")
    
        

if __name__ == "__main__":
    
    if mode == "Development":
        x = "log.txt"
        inputdir = "/home/rahul/anaconda3/bin/Edu.Data (Complete & Option-Wise )(TQ-46301)/SSC (TQ-35884)4,5 OPTION/REASONING (TQ-8832), 4-5 OPTIONS"
    elif mode == "Deploy":
        x = input("Please Input ame of log file:   ")
        inputdir = input("Enter the directiory path:    ")
        
    logging.basicConfig(level=20, filename = x)
    jpgdir_list = []
    recursefunct(inputdir)
    copypgdirrlist = copy.deepcopy(jpgdir_list)
    create_file_list(copypgdirrlist)