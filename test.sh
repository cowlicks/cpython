#!/usr/bin/env bash
set -e
clear
make
#make install
echo 'running test.py'
./test.py
