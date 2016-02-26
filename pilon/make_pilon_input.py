#!/usr/bin/env python
#This script will take the pipeline input file and make the input file for
#the make_ind_pilon.py script which looks like below.
#ERS#       frags:ERR#       jumps:ERR#       unpaired:ERR#

import sys
import os
import argparse
from string import Template

    
def get_args():    
    parser = argparse.ArgumentParser(description='Pipeline for pilon')
    parser.add_argument("input", help="pipeline input file")
    parser.add_argument("output", help="outfile name")

    return parser.parse_args()

args = get_args()

def make_dict():
    d = {}
    with open(args.input, 'r') as infile:
        for line in infile:
            line = line.strip().split()
            run = line[0]
            samp = line[1]
            strategy = line[4].lower()
            if strategy == "paired":
                info = "frags:" + run
            elif strategy == "single":
                info = "unpaired:" + run
            elif stragey == "matepair":
                info = "jumps:" + run
            else:
                print("Unrecognized sequencing strategy: {0}".format(strategy))
            if samp in d:
                d[samp].append(info)
            else:
                d[samp] = [info]
    return d

def make_input_file(d):
    with open(args.output, 'w') as outfile:
        for samp in d:
            outfile.write(samp + "\t" + "\t".join(d[samp]) + "\n")

d = make_dict()
make_input_file(d)
