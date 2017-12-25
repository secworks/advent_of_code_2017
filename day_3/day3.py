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

VERBOSE = 1


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
    my_name = coord2name(x, y)
    print("coordinate we want area for: %s" % (my_name))
    acc = 0
    for i in range(3):
        for j in range(3):
            name = coord2name((x + j -1), (y + i - 1))
            print("Testing coordinate: %s" % (name))
            if name in elements and (name != my_name):
                (state, value) = elements[name]
                acc += value
                print("Found neighbour %s with value %d" % (name, value))
    print("sum for coordingte %s: %d" % (my_name, acc))
    print("")
    return acc


#-------------------------------------------------------------------
# get_next_spiral_position()
#
# Given a set of coordinates, direction and current min-, max-
# values return the updated coordinates, direction and min-, max-
# values in the spiral pattern.
#-------------------------------------------------------------------
def get_next_spiral_position(state):
    (x, y, min_x, max_x, min_y, max_y, direction) = state

    if direction == "right":
        print("moving right")
        x += 1
        if x > max_x:
            print("turning up")
            max_x = x
            direction = "up"

    elif direction == "left":
        print("moving left")
        x -= 1
        if  x < min_x:
            print("turning down")
            min_x = x
            direction = "down"

    elif direction == "up":
        print("moving up")
        y -= 1
        if y > min_y:
            print("turning left")
            min_y = y
            direction = "left"

    elif direction == "down":
        print("moving down")
        y += 1
        if y > max_y:
            print("turning right")
            max_y = y
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
def get_element_acc(n):
    elements = {}
    ctr = 1
    acc = 1
    state = get_init_position()
    elements[coord2name(0,0)] = (state, acc)

    while (ctr < n):
        ctr += 1
        state = get_next_spiral_position(state)
        (x, y, min_x, max_x, min_y, max_y, direction) = state
        acc = get_element_sum(elements, x, y)
        elements[coord2name(x,y)] = (state, acc)

    return acc


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def part_one():
    print("Part one.")
    print("Distance for square 361527: ", num2distance(361527))
    print()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def part_two(n):
    print("Part two.")
    print("Next value after 361527: ", get_element_acc(361527))
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
#    print("Sum for square 1 (1):    ", get_element_acc(1))
#    print("Sum for square 2 (1):    ", get_element_acc(2))
#    print("Sum for square 3 (2):    ", get_element_acc(3))
#    print("Sum for square 4 (4):    ", get_element_acc(4))
    print("Sum for square 5 (5):   ", get_element_acc(5))
#    print("Sum for square 6 (10):  ", get_element_acc(6))
#   print("Sum for square 14 (122): ", part_two(14))
#   print("Sum for square 23 (806): ", part_two(23))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
#    test_one()
#    part_one()
    test_two()
#    part_two()


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_3.py
#=======================================================================
