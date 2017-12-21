#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_1.py
# --------
# Solution for Advent of code 2017, day 1.
# http://adventofcode.com/2017/day/1
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 0


#-------------------------------------------------------------------
# get_input()
#-------------------------------------------------------------------
def get_input():
    with open('my_input.txt','r') as f:
        test_string = f.read()
    return test_string.strip()


#-------------------------------------------------------------------
# parse()
#-------------------------------------------------------------------
def parse(s):
    first = s[0]
    acc = 0

    # Scan through the string and add if pairs match.
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            acc += int(s[i])

    # Handle the end case.
    if s[0] == s[-1]:
        acc += int(s[0])

    return acc


#-------------------------------------------------------------------
# parse_two()
#-------------------------------------------------------------------
def parse_two(string):
    length = len(string)
    ctr = 0;
    acc = 0;
    i = 0
    j = int(length / 2)
    while ctr < length:
        if VERBOSE:
            print("ctr: %d, acc: %d, i: %d, idata: %s, j: %d, jdata: %s" %\
                  (ctr, acc, i, string[i], j, string[j]))

        if string[i] == string[j]:
            acc = acc + int(string[i])

        i = (i + 1) % length
        j = (j + 1) % length
        ctr += 1

    return acc


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(string):
    print("Result part one: ", parse(string))
    print("")


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(string):
    print("Result part two: ", parse_two(string))
    print("")


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_one():
    print("Teststrings part one:")
    print(parse("1122"), "Should be 3")
    print(parse("1111"), "Should be 4")
    print(parse("1234"), "Should be 0")
    print(parse("91212129"), "Should be 9")
    print("")


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_two():
    print("Teststrings part two:")
    print(parse_two("1212"), "Should be 6")
    print(parse_two("1221"), "Should be 0")
    print(parse_two("123425"), "Should be 4")
    print(parse_two("123123"), "Should be 12")
    print(parse_two("12131415"), "Should be 4")
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_string = get_input()
    part_one(my_string)
    part_two(my_string)

    test_one()
    test_two()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_1.py
#=======================================================================
