#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_16.py
# --------
# Solution for Advent of code 2017, day 16.
#
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 0


#-------------------------------------------------------------------
# spin()
#
# Basically circlular right rotate.
#-------------------------------------------------------------------
def spin(step, state):
    return state[-step:] + state[:-step]


#-------------------------------------------------------------------
# exchange()
#
# Exchange elements on position a and b in the state.
#-------------------------------------------------------------------
def exchange(a, b, state):
    tmp_a = state[a]
    state[a] = state[b]
    state[b] = tmp_a
    return state


#-------------------------------------------------------------------
# find_index()
#
# Helper function. Find where in the state a given element is.
#-------------------------------------------------------------------
def find_index(a, state):
    for i in range(len(state)):
        if state[i] == a:
            return i


#-------------------------------------------------------------------
# partner()
#
# Switch places between two named partners in the state.
# Basically exchange but with names elements instead of indices.
#-------------------------------------------------------------------
def partner(a, b, state):
    ap = find_index(a, state)
    bp = find_index(b, state)
    return exchange(ap, bp, state)


#-------------------------------------------------------------------
# get_dance()
#
# Load the dance from file, parsing the moves into something
# we can easily perform.
#-------------------------------------------------------------------
def get_dance():
    if VERBOSE:
        print("Loading moves...")

    with open('my_moves.txt','r') as f:
        my_string = f.read()
    moves = my_string.split(',')
    dance = []

    for move in moves:
        if move[0] == 's':
            num = int(move[1:])
            dance.append(('spin', (num)))


        if move[0] == 'x':
            pos = move[1:].split('/')
            dance.append(('exchange', (int(pos[0]), int(pos[1]))))


        if move[0] == 'p':
            pair = move[1:].split('/')
            dance.append(('partner', (pair[0], pair[1])))

    return dance


#-------------------------------------------------------------------
# do_move()
#
# Perform one of the three different types of moves.
#-------------------------------------------------------------------
def do_move(move, state):
    (cmd, data) = move

    if cmd == 'spin':
        index = data
        return spin(index, state)

    if cmd == 'exchange':
        a, b = data
        return exchange(a, b, state)

    if cmd == 'partner':
        a, b = data
        return partner(a, b, state)


#-------------------------------------------------------------------
# do_dance()
#
# Perform a complete dance by performing all moves in
# a dance in sequence on the state.
#-------------------------------------------------------------------
def do_dance(dance, state):
    for move in dance:
        state = do_move(move, state)
    return state


#-------------------------------------------------------------------
# first_dance()
#
# Perform one dance with the given inital permutation and
# print the state after once complete dance.
#-------------------------------------------------------------------
def first_dance(dance):
    state = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    print("Performing first dance.")

    state = do_dance(dance, state)

    print("Result for first dance:")
    print("".join(state))
    print("")


#-------------------------------------------------------------------
# eq_lists()
#
# Returns True if list l1 and l2 are equal, that is of
# same length and with same elements (including order).
# List are assumed to of equal length.
#-------------------------------------------------------------------
def eq_lists(l1, l2):
    are_equal = True
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            are_equal = False
    return are_equal


#-------------------------------------------------------------------
# second_dance()
#
# The possible states after a dance are cyclic. We therefore
# perform a number of dances until the state after a complete
# dance repeats. We then find which of the states would be
# the result after 1000000000 dances.
#-------------------------------------------------------------------
def second_dance(dance):
    state = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    print("Performing second dance.")

    iterations = 1000000000
    dance_states = []
    state_loop = False
    dance_ctr = 0

    while not state_loop:
        state = do_dance(dance, state)

        if VERBOSE:
            print("State after dance %03d: " %(dance_ctr), state)

        for old_state in dance_states:
            if eq_lists(old_state, state):
                state_loop = True

        if not state_loop:
            dance_states.append(state[:])
            dance_ctr += 1

    if VERBOSE:
        print("Loop found after %d dances." % (dance_ctr))

    # We start counting on zero.
    index = (iterations % dance_ctr) - 1

    if VERBOSE:
        print("state after %011d iterations are given by index %03d" % (iterations, index))

    print("Result for second dance:")
    print("".join(dance_states[index]))
    print("")


#-------------------------------------------------------------------
# run_tests()
#
# Test the moves using the test cases from the README.
#-------------------------------------------------------------------
def run_tests():
    test_state = ['a', 'b', 'c', 'd', 'e']

    print("State before spin:            ", test_state)
    print("State after spin s1:          ", spin(1, test_state))
    print("Expected state after spin:    ", ['e', 'a', 'b', 'c', 'd'])
    print("")

    test_state = ['e', 'a', 'b', 'c', 'd']
    print("State before exhange:         ", test_state)
    print("State after exchange x3/4:    ", exchange(3, 4, test_state))
    print("Expected state after spin:    ", ['e', 'a', 'b', 'd', 'c'])
    print("")

    test_state = ['e', 'a', 'b', 'd', 'c']
    print("State before partner:         ", test_state)
    print("State after partner pe/b:     ", partner('e', 'b', test_state))
    print("Expected state after partner: ", ['b', 'a', 'e', 'd', 'c'])
    print("")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_dance = get_dance()
    first_dance(my_dance)
    second_dance(my_dance)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day16.py
#=======================================================================
