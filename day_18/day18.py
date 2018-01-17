#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_18.py
# --------
# Solution for Advent of code 2017, day 18.
# https://adventofcode.com/2017/day/18
#
#
# Status: Not done.
#
# Joachim Strömbergson 2018
#
#=======================================================================

import sys

VERBOSE = 0


#-------------------------------------------------------------------
# load_sw()
#
# Load the dance from file, parsing the moves into something
# we can easily perform.
#-------------------------------------------------------------------
def load_sw():
    program = []
    if VERBOSE:
        print("Loading program...")

    with open('my_input.txt','r') as f:
        for line in f:
            line = line.rstrip()
            program.append(line.split(' '))
    return program


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_program = load_sw()
    print(my_program)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day18.py
#=======================================================================
