#!/usr/bin/env python

import sys
import os
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Creates a dag file for decoupling interleaved fastq files')
    parser.add_argument("input", help="List of interleaved fastq file names")
    return parser.parse_args()

args = get_args()

dag = open("decouple.dag", "w")

with open(args.input, 'r') as infile:
    for line in infile:
        line = line.strip()
        inputList = line.split()
        run = [inputList[0]]
	for i in run:
		print i
		dag.write("JOB "+i+"_decouple decouple.submit\nVARS "+i+"_decouple RUN=\""+i+"\""+"\n\n")
infile.close()

