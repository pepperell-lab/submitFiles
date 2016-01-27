#!/bin/bash

java -ea -Xmx4g -cp /opt/PepPrograms/bbmap/current/ jgi.KmerNormalize bits=32 in1=$1_1.fastq in2=$1_2.fastq out=$1_out.fastq target=150
