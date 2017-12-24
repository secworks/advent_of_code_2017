#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_3.py
# --------
# Solution for Advent of code 2017, day 1.
# http://adventofcode.com/2017/day/3
#
# Status: Not done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 0


#-------------------------------------------------------------------
# get_manhattan_distance()
#
# Get the manhattan distance from a coordinate to origo.
#-------------------------------------------------------------------
def get_manhattan_distance(coord):
    x, y = coord
    return abs(x) + abs(y)


#-------------------------------------------------------------------
# coord2name()
#
# Convert coordinate to a unique name.
#-------------------------------------------------------------------
def coord2name(x, y):
    return 'x' + str(x) + '_' + 'y' + str(y)


#-------------------------------------------------------------------
# get_element_sum()
#
# Given coordinates for an element and a database of elements,
# extract the (possible) neighbour elements. Return the sum
# of all values of the neighbour elements.
#-------------------------------------------------------------------
def get_element_sum(elements, x, y):
    acc = 0
    for i in range((x - 1), 3):
        for j in range((y - 1), 3):
            name = coord2name(i, j)
            if name in elements:
                acc += elements[name]
    return acc


#-------------------------------------------------------------------
# get_spiral_position()
#
# Get the (x, y) spiral positon for a given value n where
# 1 is in (0, 0) and we move right, up, left, down,.. etc
#
# The trick is to look left in a given position.
#-------------------------------------------------------------------
def get_spiral_position(n):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    tmp_x = 0
    tmp_y = 0

    # Create db with elements and add the initial origo element.
    elements = {}
    elements[coord2name(tmp_x, tmp_y)] = 1

    square = 1
    direction = "right"

    while square < n:
        square += 1
        if VERBOSE > 0:
            print("square %d" % square)

        if direction == "right":
            if VERBOSE > 1:
                print("moving right")
            tmp_x += 1
            if tmp_x > max_x:
                if VERBOSE > 1:
                    print("turning up")
                max_x = tmp_x
                direction = "up"

        elif direction == "left":
            if VERBOSE > 1:
                print("moving left")
            tmp_x -= 1
            if tmp_x < min_x:
                if VERBOSE > 1:
                    print("turning down")
                min_x = tmp_x
                direction = "down"

        elif direction == "up":
            if VERBOSE > 1:
                print("moving up")
            tmp_y += 1
            if tmp_y > max_y:
                if VERBOSE > 1:
                    print("turning left")
                max_y = tmp_y
                direction = "left"

        elif direction == "down":
            if VERBOSE > 1:
                print("moving down")
            tmp_y -= 1
            if tmp_y < min_y:
                if VERBOSE > 1:
                    print("turning right")
                min_y = tmp_y
                direction = "right"

        # Get set of value from elements around the given element.
        # Add the element with the sum to the database
        elem_sum = get_element_sum(elements, tmp_x, tmp_y)
        elements[coord2name(tmp_x, tmp_y)] = elem_sum


    return (tmp_x, tmp_y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def part_one():
    print("Part one.")
    print("Distance for square 361527: ", get_manhattan_distance(get_spiral_position(361527)))
    print()

#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_one():
    print("Tests coordinates:")
    print("Distance for square 1:    ", get_manhattan_distance(get_spiral_position(1)))
    print("Distance for square 12:   ", get_manhattan_distance(get_spiral_position(12)))
    print("Distance for square 23:   ", get_manhattan_distance(get_spiral_position(23)))
    print("Distance for square 1024: ", get_manhattan_distance(get_spiral_position(1024)))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    test_one()
    part_one()

    print(coord2name(2, -4))

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_3.py
#=======================================================================
