submitFiles
===========

Condor submit files (and executable where applicable)

File Descriptions
=================
fasttree.submit
---------------
This submit file executes the fasttree program from the /opt/PepPrograms folder. The "10" in the arguments line specifies the desired number of threads, while the "dummy_snps.fasta" corresponds to the input file (your snp alignment). 

>condor_submit fasttree.submit

run_parsnp.submit
-----------------
This submit file executes a corresponding bash script (run_parsnp.sh) with three arguments: a compressed folder (.tar.gz) containing the genomes to be assembled (fasta format), the path to the reference genome (stored in opt/data), and the number of threads to use.

>condor_submit run_parsnp.submit

run_parsnp.sh
-------------
This is a simple bash script that will unpack the compressed genomes, make and move them into a directory, execute parsnp, and finally compress parsnp's output (a folder containing various files) so that it can be transferred back. 

blast.submit
------------
This submit file runs blastp of files named $(PROCESS).tsv against a blast
database (which is transferred with the jobs).

RAxML
------------
Folder contains three submit files, one for each step of generating a bootstrapped ML tree with RAxML. "bestTree" and "bootstrap" steps can be run at the same time. Threads can differ between jobs. Dag needs to be edited with alignment name, desired output suffixes, and the number of threads. Requested memory and space is based on an alignment of ~600 Mtb samples and may not reflect others needs - please change as needed for your purposes.

>condor_submit_dag RAxML.dag
