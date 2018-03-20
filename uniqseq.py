#!/usr/bin/env python3
## Remove duplicated protein/nucleic acid sequences, keeping the first occurrence. 
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse


## Classes

## Functions

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Remove duplicated protein/nucleic acid sequences, keeping the first occurrence. If not input file given it reads from the standard input and if not output file given it writes to standard output.")
    parser.add_argument('-v', '--version', action='version', version='0.0.1', help="Show program's version number and exit.")
    

    args=parser.parse_args()


## Running the script
if __name__ == "__main__":
        main()

