#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_2.py
# --------
# Solution for Advent of code 2017, day 2.
# http://adventofcode.com/2017/day/2
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input():
    my_input = []
    with open('my_input.txt','r') as f:
        for line in f:
            my_string = line.split()
            my_input.append(my_string)
    return my_input


#-------------------------------------------------------------------
# get_divisor()
#
# Search through the list with two pointers to find the two
# numbers that are evenly divisable. Return the divisor.
#-------------------------------------------------------------------
def get_divisor(line):
    num = 0
    dom = 0
    for i in range(len(line)):
        ival = int(line[i])
        for j in range(len(line)):
            jval = int(line[j])
            if (i != j) and (ival % jval == 0):
                num = ival
                dom = jval
    return int(num / dom)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def second_part(my_input):
    acc = 0
    for line in my_input:
        acc += get_divisor(line)
    print("Part two - sum of divisors: %d" %(acc))


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
    return maxval - minval


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def first_part(my_input):
    acc = 0
    for line in my_input:
        acc += get_diff(line)
    print("Part one - sum of differences: %d" %(acc))
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
    my_input = get_input()
    first_part(my_input)
    second_part(my_input)




#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_2.py
#=======================================================================
