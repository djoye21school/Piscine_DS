#!/bin/sh
sed -E '/\"[Dd]ata [Ss]cientist\"/! s/[^"]*[Jj]unior[^"]*/Junior/g; s/[^"]*[Mm]iddle[^"]*/Middle/g; s/[^"]*[Ss]enior[^"]*/Senior/g; s/[^"]*[Dd]ata[^"]*/-/g; s/[^"]*[Аа]налит[^"]*/-/g' $1 > hh_positions.csv
