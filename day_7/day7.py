#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day9.py
# --------
# Solution for Advent of code 2017, day 7.
# http://adventofcode.com/2017/day/7
#
# Status: Not done.
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
    data = []
    with open('my_input.txt','r') as f:
        for line in f:
            data.append(line.strip())
    return data


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def build_db(s):
    db = {}
    for e in s:
        if "->" in e:
            splitline = e.split()
            name = splitline[0]
            weight = splitline[1][1:-1]
            children = splitline[3:]
            db[name] = ("node", weight, children)

        else:
            name, weight = e.split()
            weight = weight[1:-1]
            db[name] = ("leaf", weight)

    return db


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_root(db):
    # Get a list of all nodes.
    nodes = []
    for e in db:
        if db[e][0] == "node":
            nodes.append(e)
    print("Nodes:", nodes)

    root = ""
    for n in nodes:
        for i in nodes:
            children = db[i][2]
            if n != i:
                print(db[i][2])



#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(s):
    db = build_db(s)
    root = find_root(db)
    print("Result part one: ")
    print("")


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(s):
    print("Result part two: ")
    print("")


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_one():
    print("Tests part one:")
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
# EOF day7.py
#=======================================================================
