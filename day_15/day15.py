#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_15.py
# --------
# Solution for Advent of code 2017, day 15.
# http://adventofcode.com/2017/day/15
#
# Status: Done.
#
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 0

#-------------------------------------------------------------------
# next_state()
# A linear congurential PRNG that given a previous state
# calculates the next state.
#-------------------------------------------------------------------
def next_state(prev_state, multiplier, divider):
    return (prev_state * multiplier) % divider


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def next_mod_state(prev, mult, divide, modulus):
    ns = next_state(prev, mult, divide)

    while (ns % modulus != 0):
        ns = next_state(ns, mult, divide)
    return ns


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def first_part():
    a_state = 277
    a_mult  = 16807
    a_div   = 2147483647

    b_state = 349
    b_mult  = 48271
    b_div   = 2147483647

    iterations = 5000000
    coll_ctr = 0

    for i in range(iterations):
        a_state = next_state(a_state, a_mult, a_div)
        a_bits = "{0:032b}".format(a_state)[16:32]
        b_state = next_state(b_state, b_mult, b_div)
        b_bits = "{0:032b}".format(b_state)[16:32]

        if a_bits == b_bits:
            coll_ctr += 1

        if VERBOSE:
            print("{0:012d}".format(a_state), "{0:012d}".format(b_state))
            print("%s %s" % (a_bits, b_bits))

    print("Second part.")
    print("Number of collisions: %d" % coll_ctr)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def second_part():
#    a_state = 65
    a_state = 277
    a_mult  = 16807
    a_div   = 2147483647
    a_mod   = 4

#    b_state = 8921
    b_state = 349
    b_mult  = 48271
    b_div   = 2147483647
    b_mod   = 8

    coll_ctr = 0
    for i in range(5000000):
        a_state = next_mod_state(a_state, a_mult, a_div, a_mod)
        a_bits = "{0:032b}".format(a_state)[16:32]
        b_state = next_mod_state(b_state, b_mult, b_div, b_mod)
        b_bits = "{0:032b}".format(b_state)[16:32]

        if a_bits == b_bits:
            coll_ctr += 1

    print("Second part:")
    print("Number of collisions: %d" % coll_ctr)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
#    first_part()
    second_part()

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
#=======================================================================
