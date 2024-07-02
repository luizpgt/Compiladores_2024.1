#!/bin/bash

set -xe

export PYTHONPATH=$PYTHONPATH:./Lexical_analysis
export PYTHONPATH=$PYTHONPATH:./Lexical_analysis/Deterministic_finite_automaton

clear
python main.py $1 # lex || parse
