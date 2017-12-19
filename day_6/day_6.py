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

    print(state)
    return state


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    state = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

    prev_states = []
    loop = False

    while not loop:
        prev_states.append(state[:])
        state = distribute(state)
        loop = check_loop(state, prev_states)

    print("Loop found after %d updates" % (len(prev_states)))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_6.py
#=======================================================================
