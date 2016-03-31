#!/bin/sh

export MUGSY_INSTALL=/opt/PepPrograms/mugsy_x86-64-v1r2.3/
export PATH=$MUGSY_INSTALL:$MUGSY_INSTALL/mapping:$PATH
export PERL5LIB=$MUGSY_INSTALL/perllibs

prefix=$1
shift
mugsy --directory . --prefix $prefix "$@"
