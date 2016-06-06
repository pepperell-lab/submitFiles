#!/bin/sh

/opt/PepPrograms/sratoolkit.2.5.2-ubuntu64/bin/fastq-dump.2.5.2 --split-files $1
/opt/PepPrograms/plasmid-SPAdes-3.5.0-Linux/bin/spades.py -1 $1_1.fastq -2 $1_2.fastq -t 8 -o $1_assembly
prokka --locustag $1 --prefix $1_plasmid --cpus 8 --genus $2 --species $3 --strain $4 --usegenus $1_assembly/scaffolds.fasta
grep 'ESX' $1_plasmid/$1_plasmid.gff
mkdir output
mv * output/
zip -r $1_assembly.zip output/$1_assembly
zip -r $1_annotation.zip output/$1_plasmid
