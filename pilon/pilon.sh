#!/bin/bash

java -jar /opt/PepPrograms/pilon-1.16.jar --genome $1 --frags $2 --output $3 --changes --vcf --tracks
