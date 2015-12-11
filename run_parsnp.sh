#!/bin/bash

tar -xzvf $1

mkdir genomes

mkdir gtfs

mv *fasta genomes

mv *gtf gtfs

/opt/PepPrograms/Parsnp-Linux64-v1.2/parsnp -r $2 -d genomes -o parsnp_output -p $3 -c -x

tar -czvf parsnp_output.tar.gz parsnp_output
