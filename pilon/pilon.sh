#!/bin/bash

java -jar /opt/PepPrograms/pilon-1.16.jar --genome $1 --$4 $2 --output $3 --variant --mindepth 10 --minmq 40 --minqual 20
