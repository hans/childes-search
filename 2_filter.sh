#!/bin/bash


python -mdep_tregex grep 'mod cpostag "adj" and deprel "MOD" and <--. (w2 cpostag "n")' < $1 \
  | python -mdep_tregex shuf \
  | awk '/adj/ {sawAdj=1; adj=$2; next} /n/ {if (sawAdj) print adj, $2; sawAdj=0; next} {sawAdj=0}' \
  | awk -f classify.awk
