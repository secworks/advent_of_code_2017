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
# Node()
#
# A simple class used as struct for node information.
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
    db = {}

    for e in s:
        if '->' in e:
            ntype = 'parent'
            name = e.split('->')[0].split()[0]
            weight = e.split('->')[0].split()[1][1:-1]
            children = e.split('->')[1].replace(',', '').split()

        else:
            ntype = 'leaf'
            name, weight = e.split()
            weight = weight[1:-1]
            children = None

        node = Node(name, ntype, weight, children)
        db[name] = node
    return db


#-------------------------------------------------------------------
# build_tree()
#
# Given a db of nodes and the name of the root, we recursively
# build upp the tree until all nodes have been added.
#-------------------------------------------------------------------
def build_tree(root, nodes):
    node = nodes.pop(root)
    if node.type != 'leaf':
        node.children = [build_tree(n, nodes) for n in node.children]
    return node


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
        n.add(node)
        if nodes[node].type == 'leaf':
            children.add(node)

        elif nodes[node].type == 'parent':
            children.update(nodes[node].children)
    return n.difference(children).pop()


#-------------------------------------------------------------------
# find_unbalanced_node()
#
# Traverse a given tree depth first checking the weight of
# all subtrees for each node. If the subtree is not unbalanced
# return the name and weight of the unbalanced node.
#-------------------------------------------------------------------
def find_unbalanced_node(node):
    if node.type == 'leaf':
        # Leaf nodes are always balanced and just returns
        # its own name and weight
        return (True, node.name, node.weight, node.weight)

    else:
        # Get balanced status from all children.
        children = [find_unbalanced_node(n) for n in node.children]
        acc = 0
        for child in children:
            (balanced, cname, cweight, nweight) = child
            acc += int(nweight)
            if not balanced:
                #Propagate unbalanced node upwards.
                return child

        if acc != int(node.weight):
            # This node is the one with incorrect weight and
            # should propagate info upwards
            print("Unbalanced node!", node.name, acc, node.weight)
            return (False, node.name, acc, node.weight)

        else:
            return (True, node.name, acc, node.weight)


#-------------------------------------------------------------------
# part_one()
#-------------------------------------------------------------------
def part_one(s):
    my_nodes= build_nodelist(s)
    root = find_root(my_nodes)
    print("Result part one: %s" % (root))
    print("")


#-------------------------------------------------------------------
# part_two()
#-------------------------------------------------------------------
def part_two(s):
    my_nodes= build_nodelist(s)
    root = find_root(my_nodes)
    my_tree = build_tree(root, my_nodes)
    unbalanced = find_unbalanced_node(my_tree)

    print("Result part two: ")
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
# EOF day7.py
#=======================================================================
