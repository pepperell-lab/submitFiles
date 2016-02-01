#!/bin/bash

paste - - - - - - - - < $1_out.fastq \
    | tee >(cut -f 1-4 | tr '\t' '\n' > $1_sub_1.fastq) \
    | cut -f 5-8 | tr '\t' '\n' > $1_sub_2.fastq
