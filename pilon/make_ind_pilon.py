#!/usr/bin/env python
#This script will take a list of sample names followed by the 'type':run#.
#ERS#       frags:ERR#       jumps:ERR#       unpaired:ERR#

import sys
import os
import argparse
from string import Template

    
def get_args():    
    parser = argparse.ArgumentParser(description='Pipeline for pilon')
    parser.add_argument("input", help="Sample Name (ERS#), unpaired/frags/jumps:ERR#")
    parser.add_argument("reference", help="Path to fasta file of reference genome, e.g. /opt/data/mtuberculosis/H37Rv.fa")
    parser.add_argument("pathtobam", help="path to folder containing bams")

    return parser.parse_args()

args = get_args()

def make_dict():
    d = {}
    with open(args.input, 'r') as infile:
        for line in infile:
            line = line.strip().split()
            d[line[0]] = []
            for run in line[1:]:
                d[line[0]].append(run)
    return d

def make_submit_files(d):
    for sample in d:
        transferFiles = []
        for i in d[sample]:
            strat,run = i.split(":")
            bam = args.pathtobam + run + ".realn.bam"
            transferFiles.append(bam)
            bai = args.pathtobam + run + ".realn.bai"
            transferFiles.append(bai)
        outfilename = sample + '_pilon.submit'
        with open(outfilename, 'w') as outfile:
            outfile.write("universe = vanilla\n\
executable = {0}_pilon.sh\n\
\n\
output = {0}.out\n\
error = {0}.err\n\
log = {0}.log\n\
\n\
should_transfer_files = YES\n\
when_to_transfer_output = ON_EXIT\n\
transfer_input_files = {1}\n\
\n\
request_cpus = 1\n\
request_memory = 2GB\n\
request_disk = 2GB\n\
\n\
queue".format(sample, ",".join(transferFiles)))

def make_sh_files(d):
    for sample in d:
        arguments = []
        for i in d[sample]:
            strat,run = i.split(":")
            single = "--" + strat + " " + run + ".realn.bam"
            arguments.append(single)
        outfilename = sample + '_pilon.sh'
        with open(outfilename, 'w') as outfile:
            outfile.write("#!/bin/bash\n\njava -jar -Xmx2g /opt/PepPrograms/pilon-1.16.jar --genome {0} {1} --output {2}_pilon --variant --mindepth 10 --minmq 40 --minqual 20".format(args.reference, " ".join(arguments), sample))

def make_dag(d):
    outfilename = args.input.split(".")[0] + ".dag"
    with open(outfilename, 'w') as outfile:
        for sample in d:
            outfile.write("JOB {0} {0}_pilon.submit\n\n".format(sample))

d = make_dict()
make_submit_files(d)
make_sh_files(d)
make_dag(d)
