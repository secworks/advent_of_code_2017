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
def get_manhattan_distance(x, y):
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
                (state, value) = elements[name]
                acc += value
    return acc


#-------------------------------------------------------------------
# get_next_spiral_position()
#
# Given a set of coordinates, direction and current min-, max-
# values return the updated coordinates, direction and min-, max-
# values in the spiral pattern.
#
# The trick is to look left in a given position.
#-------------------------------------------------------------------
def get_next_spiral_position(state):
    (x, y, min_x, max_x, min_y, max_y, direction) = state

    if direction == "right":
        if VERBOSE > 1:
            print("moving right")
        x += 1
        if x > max_x:
            if VERBOSE > 1:
                print("turning up")
            max_x = x
            direction = "up"

    elif direction == "left":
        if VERBOSE > 1:
            print("moving left")
        x -= 1
        if  x < min_x:
            if VERBOSE > 1:
                print("turning down")
            min_x = x
            direction = "down"

    elif direction == "up":
        if VERBOSE > 1:
            print("moving up")
        y += 1
        if y > max_y:
            if VERBOSE > 1:
                print("turning left")
            max_y = y
            direction = "left"

    elif direction == "down":
        if VERBOSE > 1:
            print("moving down")
        y -= 1
        if y < min_y:
            if VERBOSE > 1:
                print("turning right")
            min_y = y
            direction = "right"

    return (x, y, min_x, max_x, min_y, max_y, direction)


#-------------------------------------------------------------------
# get_init_position
#
# (x, y, min_x, max_x, min_y, max_y, dir)
#-------------------------------------------------------------------
def get_init_position():
    return (0, 0, 0, 0, 0, 0, "right")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def num2distance(n):
    my_state = get_init_position()
    ctr = 1
    while ctr < n:
        my_state = get_next_spiral_position(my_state)
        ctr += 1
    (x, y, min_x, max_x, min_y, max_y, direction) = my_state
    return get_manhattan_distance(x, y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def part_one():
    print("Part one.")
    print("Distance for square 361527: ", num2distance(361527))
    print()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def part_two():
    print("Part two.")

    elements = {}
    acc = 1
    state = get_init_position()
    elements[coord2name(0,0)] = (state, acc)

    while (acc <= 361527):
        state = get_next_spiral_position(state)
        (x, y, min_x, max_x, min_y, max_y, direction) = state
        acc = get_element_sum(elements, x, y)
        elements[coord2name(x,y)] = (state, acc)

    print("Next value after 361527: ", acc)
    print()


#-------------------------------------------------------------------
# test_one()
#-------------------------------------------------------------------
def test_one():
    print("Tests coordinates:")
    print("Distance for square 1:    ", num2distance(1))
    print("Distance for square 12:   ", num2distance(12))
    print("Distance for square 23:   ", num2distance(23))
    print("Distance for square 1024: ", num2distance(1024))
    print("")


#-------------------------------------------------------------------
# test_two()
#-------------------------------------------------------------------
def test_two():
    print("Tests sums:")
    print("Sum for square 2 (1):    ", num2distance(1))
    print("Sum for square 4 (4):    ", num2distance(1))
    print("Sum for square 6 (10):   ", num2distance(1))
    print("Sum for square 14 (122): ", num2distance(12))
    print("Sum for square 23 (806): ", num2distance(23))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    test_one()
    part_one()
    test_two()
    part_two()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_3.py
#=======================================================================
