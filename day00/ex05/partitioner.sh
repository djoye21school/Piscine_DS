#!/bin/sh
awk -F '\",\"|T' 'NR==1 {h=$0; next} {f=$2".csv"} !($2 in p) {p[$2]; print h > f} {print >> f}' $1
