#!/bin/sh
(cat $1 | head -n 1; cat $1 | tail -n +2 | sort -t ',' -k 2 -k 1n) > hh_sorted.csv
