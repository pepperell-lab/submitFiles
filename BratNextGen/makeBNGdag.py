#!/usr/bin/env python
#This script creates a dag file for submitting the individual files created by makeBNGsubmit.py

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Creates a dag file for running 100 permutations of BratNextGen')
    return parser.parse_args()

args = get_args()

dag = open("BNGperm.dag", "w")

for i in range(1,101):
	dag.write("JOB "+str(i)+"_BNGperm "+str(i)+"_BNGperm.submit\n\n")


