#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day9.py
# --------
# Solution for Advent of code 2017, day 9.
# http://adventofcode.com/2017/day/9
#
# Status: Not done.
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
    stripped = test_string.strip()
    return stripped


#-------------------------------------------------------------------
# filter_garbage()
#
# Given a string s, returns a filtered version of s where
# garbage has been removed.
#-------------------------------------------------------------------
def filter_garbage(s):
    fs = ""
    slen = len(s)
    in_garbage = False
    i = 0

    while i < len(s):
        if s[i] == '!' and in_garbage:
            i += 2

        elif s[i] == '>' and in_garbage:
            in_garbage = False
            i += 1

        elif s[i] == '<' and not in_garbage:
            in_garbage = True
            i += 1

        else:
            if not in_garbage:
                fs += s[i]
            i += 1

    return fs


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_score(s):
    return 2


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_groups(s):
    return 2


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(string):
    print("Result part one: ")
    print("")


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(string):
    print("Result part two: ")
    print("")


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_one():
    print("Tests part one:")
    print("Check number of groups:")
    print("'{}' should be 1 group: ", get_groups('{}'))
    print("'{{{}}}' should be 3 groups: ", get_groups('{{{}}}'))
    print("'{{},{}}' should be 3 groups: ", get_groups('{{},{}}'))
    print("'{{{},{},{{}}}}' should be 6 groups: ", get_groups('{{{},{},{{}}}}'))
    print("'{<{},{},{{}}>}' should be 1 group with garbage: ", get_groups('{<{},{},{{}}>}'))
    print("'{<a>,<a>,<a>,<a>}' should be 1 group: ", get_groups('{<a>,<a>,<a>,<a>}'))
    print("'{{<a>},{<a>},{<a>},{<a>}}' should be 5 groups: ", get_groups('{{<a>},{<a>},{<a>},{<a>}}'))
    print("'{{<!>},{<!>},{<!>},{<a>}}' should be 2 groups: ", get_groups('{{<!>},{<!>},{<!>},{<a>}}'))
    print()

    print("Check scores:")
    print("'{}' should be 1: ", get_score('{}'))
    print("'{{{}}}' should be 6 ", get_score('{{{}}}'))
    print("'{{},{}}' should be 5: ", get_score('{{},{}}'))
    print("'{{{},{},{{}}}}' should be 16: ", get_score('{{{},{},{{}}}}'))
    print("'{<a>,<a>,<a>,<a>}' should be 1: ", get_score('{<a>,<a>,<a>,<a>}'))
    print("'{{<ab>},{<ab>},{<ab>},{<ab>}}' should be 9: ", get_score('{{<ab>},{<ab>},{<ab>},{<ab>}}'))
    print("'{{<!!>},{<!!>},{<!!>},{<!!>}}' should be 9: ", get_score('{{<!!>},{<!!>},{<!!>},{<!!>}}'))
    print("'{{<a!>},{<a!>},{<a!>},{<ab>}}' should be 3: ", get_score('{{<a!>},{<a!>},{<a!>},{<ab>}}'))
    print()


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_two():
    print("Tests part two:")
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_input = get_input()
    print(my_input)
    print()
    print(filter_garbage(my_input))

#    test_one()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day9.py
#=======================================================================
