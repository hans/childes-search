#!/bin/bash
set -e

# Produce a list of verb roots appearing in a parsed corpus.

export PYTHONPATH=dep_tregex
python -m dep_tregex grep "root deprel 'ROOT' and cpostag 'v'" < $1 \
  | awk '$4 == "v" {split($2,a,"-"); print a[1]}'
