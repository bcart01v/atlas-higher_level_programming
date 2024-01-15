#!/bin/bash

# Check if a program name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <program_name>"
    exit 1
fi

# Assign the program name to a variable
PROGRAM_NAME=$1

# Run the doctest module on the provided program
python3 -m doctest -v ./tests/$PROGRAM_NAME.txt
