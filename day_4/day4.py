#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_4.py
# --------
# Solution for Advent of code 2017, day 4.
# http://adventofcode.com/2017/day/4
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys


#-------------------------------------------------------------------
# get_input()
# Load the input data to thechallenge from file.
# Split the data into lists of strings.
#-------------------------------------------------------------------
def get_input():
    my_input = []
    with open('my_input.txt','r') as f:
        for line in f:
            my_string = line.split()
            my_input.append(my_string)
    return my_input


#-------------------------------------------------------------------
# no_anagram_dup_words()
#
# For each word in a given list we match its length against
# all other words. If the lengths of two worfds are the same we
# create a set of the letters in each word and then check if the
# sets are equal or not.
#-------------------------------------------------------------------
def no_anagram_dup_words(line):
    for i in range(len(line)):
        for j in range(len(line)):
            if (i != j) and len(line[i]) == len(line[j]):
                i_set = {a for a in line[i]}
                j_set = {a for a in line[j]}
                if i_set <= j_set:
                    return False
    return True


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(my_input):
    acc = 0
    for line in my_input:
        if no_anagram_dup_words(line):
            acc += 1
    print("Part two - no anagram duplicate words.")
    print("Number of passphrases: %d" % (len(my_input)))
    print("Number of valid passphrases: %d" % (acc))
    print("")


#-------------------------------------------------------------------
# no_dup_words()
#
# Find dunplicate words in a given line. Simple n**2
# method where we match every words with every other word.
#-------------------------------------------------------------------
def no_dup_words(line):
    for i in range(len(line)):
        for j in range(len(line)):
            if i != j and line[i] == line[j]:
                return False
    return True


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(my_input):
    acc = 0
    for line in my_input:
        if no_dup_words(line):
            acc += 1
    print("Part one - no duplicate words.")
    print("Number of passphrases: %d" % (len(my_input)))
    print("Number of valid passphrases: %d" % (acc))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_input = get_input()
    part_one(my_input)
    part_two(my_input)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_2.py
#=======================================================================
