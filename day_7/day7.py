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
#-------------------------------------------------------------------
class Node:
    def __init__(self, name, ntype, weight, children = None):
        self.name = name
        self.type = ntype
        self.weight = weight
        self.children = children


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
# build_nodelist()
#
# Parse the given input a create a list of nodes with their
# type, name etc for each node.
#-------------------------------------------------------------------
def build_nodelist(s):
    db = []
    for e in s:
        if "->" in e:
            splitline = e.split()
            name = splitline[0]
            weight = splitline[1][1:-1]
            children = splitline[3:]
            node = Node(name, "parent", weight, children)
            db.append(node)

        else:
            name, weight = e.split()
            weight = weight[1:-1]
            node = Node(name, "leaf", weight, None)
            db.append(node)

    return db


#-------------------------------------------------------------------
# find_root(nodes)
#
# Given a list of nodes, walk through the nodes. If a node is
# parent node, add its children to a set of all children. We also
# save the names of all parents in a list. We then walk through
# the list of parents to find which parent node is not in the set.
# That node is not itself a child and thus the root parent.
#-------------------------------------------------------------------
def find_root(nodes):
    children = set()
    parents = []

    for node in nodes:
        if node.type == "parent":
            parents.append(node.name)
            children.update(node.children)

    for name in parents:
        if name not in children:
            print("probably root:", name)


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(s):
    my_nodes= build_nodelist(s)
    root = find_root(my_nodes)
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
