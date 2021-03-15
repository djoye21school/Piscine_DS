#!/bin/sh
jq -rf filter.jq $1 > hh.csv
