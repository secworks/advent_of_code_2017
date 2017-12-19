#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_6.py
# --------
# Solution for Advent of code 2017, day 6.
# http://adventofcode.com/2017/day/6
#
# Status: Not done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys


#-------------------------------------------------------------------
# check_loop()
#
# Given a state and a set of states, check if the state
# is present among the states.
#-------------------------------------------------------------------
def check_loop(state, states):
    for prev in states:
        if state == prev:
            return True
    return False


#-------------------------------------------------------------------
# distribute()
#
# Given a list with block allocations in a set of banks,
# locate the bank with maximum number of blocks. Then
# distribute these blocks in a round robin order.
#-------------------------------------------------------------------
def distribute(state):
    # Find bank with most blocks.
    ip = 0
    i = state[ip]
    for j in range(len(state) - 1):
        if state[(j + 1)] > i:
            ip = (j + 1)
            i = state[(j + 1)]

    # Clear block counter at the bank with most blocks.
    state[ip] = 0

    # Distribute the number of blocks over the other banks.
    while i > 0:
        ip = (ip + 1) % len(state)
        state[ip] = state[ip] + 1
        i -= 1

    return state


#-------------------------------------------------------------------
# part_two()
#
# Find how many state updates are needed to get back to the
# given init state.
#-------------------------------------------------------------------
def part_two(init_state):

    new_state = init_state[:]
    done = False
    ctr = 0

    while not done:
        ctr += 1
        new_state = distribute(new_state)
        if new_state == init_state:
            done = True

    print("Part two.")
    print("Init state recreated after %d updates" % (ctr))
    print("")


#-------------------------------------------------------------------
# part_one()
#
# Detect loop in state starting from a given state.
#-------------------------------------------------------------------
def part_one(init_state):
    state = init_state[:]
    prev_states = []
    loop = False

    while not loop:
        prev_states.append(state[:])
        state = distribute(state)
        loop = check_loop(state, prev_states)

    print("Part one.")
    print("Loop found after %d updates" % (len(prev_states)))
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_state = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
    part_one(my_state)
    part_two(my_state)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_6.py
#=======================================================================
