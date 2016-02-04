#!/usr/bin/env python
#This script will take a list of sample names and create a generic job for each.
#ERR071082       ERS088906       ERX048850       illumina        paired

import sys
import os
import argparse
from string import Template

    
def get_args():    
    parser = argparse.ArgumentParser(description='Pipeline for reference \
guided assembly')
    parser.add_argument("input", help="File describing read data information")
    parser.add_argument("reference", help="Fasta file of reference genome")
    parser.add_argument("dagtemplate", help="dag template")
    parser.add_argument("outfilename", help="out.dag")

    return parser.parse_args()

args = get_args()

with open(args.dagtemplate, "r") as template_file:
    template = Template(template_file.read())

with open(args.input, 'r') as infile, open(args.outfilename, 'w') as dagfile:
    for line in infile:
        line = line.strip()
        inputList = line.split()
        variableMap = {}
        variableMap['ref'] = args.reference
        variableMap['run'] = inputList[0]
        #variableMap['sample'] = inputList[1]
        #variableMap['lib'] = inputList[2]
        #variableMap['platform'] = inputList[3].lower()
        #pair = inputList[4].lower()
        out = template.substitute(variableMap)
        dagfile.write(out + '\n')

    

