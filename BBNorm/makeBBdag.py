#!/usr/bin/env python

import sys
import os
import argparse
    
def get_args():
    parser = argparse.ArgumentParser(description='Creates a dag file for multiple fastq files to be normalized using BBNorm')
    parser.add_argument("input", help="List of fastq file names")
    return parser.parse_args()

args = get_args()

dag = open("BBNorm.dag", "w")

with open(args.input, 'r') as infile:
    for line in infile:
        line = line.strip()
        inputList = line.split()
        run = [inputList[0]]
	for i in run:
		print i
		dag.write("JOB "+i+"_BBNorm BBNorm.submit\nVARS "+i+"_BBNorm RUN=\""+i+"\""+"\n\n")
infile.close()
    

