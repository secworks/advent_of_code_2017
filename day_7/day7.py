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
# type, name etc for each node. We do some really hairy
# parsing with strip, split, replace and subscripting.
#-------------------------------------------------------------------
def build_nodelist(s):
    db = []
    pctr = 0
    cctr = 0

    for e in s:
        if '->' in e:
            ntype = 'parent'
            name = e.split('->')[0].split()[0]
            weight = e.split('->')[0].split()[1][1:-1]
            children = e.split('->')[1].replace(',', '').split()
            pctr += 1

        else:
            ntype = 'leaf'
            name, weight = e.split()
            weight = weight[1:-1]
            children = None
            cctr += 1

        node = Node(name, ntype, weight, children)
        db.append(node)
    return db


#-------------------------------------------------------------------
# find_root(nodes)
#
# Given a list of nodes, walk through the nodes and create two
# sets. One with all nodes and one with all children. The root is
# then the node among all nodes that is not also a child.
#-------------------------------------------------------------------
def find_root(nodes):
    children = set()
    n = set()

    # Create set with all children.
    for node in nodes:
        n.add(node.name)
        if node.type == 'leaf':
            children.add(node.name)

        elif node.type == 'parent':
            children.update(node.children)
    return n.difference(children)


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(s):
    my_nodes= build_nodelist(s)
    root = find_root(my_nodes)
    print("Result part one: ", root)
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
