#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day9.py
# --------
# Solution for Advent of code 2017, day 9.
# http://adventofcode.com/2017/day/9
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 0
RUN_TESTS = 0

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
    ctr = 0
    i = 0

    while i < slen:
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
            else:
                ctr += 1
            i += 1

    return fs, ctr


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_groups_score(s):
    fs, ctr = filter_garbage(s)
    groups = 0
    group_level = 0
    acc = 0
    slen = len(fs)
    i = 0

    while i < slen:
        if fs[i] == '{':
            group_level += 1

        if fs[i] == '}':
            acc += group_level
            groups += 1
            group_level -= 1

        i += 1

    return groups, acc


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_garbage(s):
    fs, ctr = filter_garbage(s)
    return ctr


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_groups(s):
    groups, acc = get_groups_score(s)
    return groups


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_score(s):
    groups, acc = get_groups_score(s)
    return acc


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(s):
    print("Result part one: ")
    print("Score for my input:", get_score(s))
    print("")


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(s):
    print("Result part two: ", get_garbage(s))
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
    print("Check amount of garbage:")
    print("'<>' should be 0: ", get_garbage('<>'))
    print("'<123451234512345>' should be 15: ", get_garbage('<123451234512345>'))
    print("'<<<<>' should be 3: ", get_garbage('<<<<>'))
    print("'<{!>}>' should be 2: ", get_garbage('<{!>}>'))
    print("'<!!>' should be 0: ", get_garbage('<!!>'))
    print("'<!!!>>' should be : ", get_garbage('<!!!>>'))
    print("'<{oxi!a,<{i<a>' should be 10: ", get_garbage('<{oxi!a,<{i<a>'))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
   my_input = get_input()

   if RUN_TESTS:
       test_one()
       test_two()
   else:
       part_one(my_input)
       part_two(my_input)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day9.py
#=======================================================================
