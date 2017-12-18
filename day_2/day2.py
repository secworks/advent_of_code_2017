#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_2.py
# --------
# Solution for Advent of code 2017, day 2.
# http://adventofcode.com/2017/day/2
#
# Status: Not done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 1

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input():
    my_input = []
    with open('my_input.txt','r') as f:
        for line in f:
            print(line)
            my_string = line.split()
            my_input.append(my_string)
    return my_input


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_diff(line):
    minval = int(line[0])
    maxval = 0
    for i in line:
        ival = int(i)
        if ival <= minval:
            minval = ival
        elif ival > maxval:
            maxval = ival

    print(minval, maxval, (maxval - minval))
    return maxval - minval


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
    my_input = get_input()
    acc = 0
    for line in my_input:
        acc += get_diff(line)
    print(acc)




#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_1.py
#=======================================================================
