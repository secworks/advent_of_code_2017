#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_5.py
# --------
# Solution for Advent of code 2017, day 5.
# http://adventofcode.com/2017/day/5
#
# Status: Not done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 1


#-------------------------------------------------------------------
# get_input()
#-------------------------------------------------------------------
def get_input():
    code = []
    with open('my_input.txt','r') as f:
        for line in f:
            code.append(int(line.strip()))
    return code


#-------------------------------------------------------------------
# part_one()
# Execute the jumps in the given code including that we increase
# the offset in each jump instruction that we executed.
#
# Exit the code when the jump ends up outside of the code.
# Print how many cycles it took.
#-------------------------------------------------------------------
def part_one(code):
    print("Part one:")
    ctr = 0
    pc = 0
    codelen = len(code)
    offset = 0
    while pc >= 0 and pc < codelen:
        offset = code[pc]
        code[pc] = code[pc] + 1
        pc = pc + offset
        ctr += 1

    print("Exited code at pc = %d after %d cycles." % (pc, ctr))
    print()


#-------------------------------------------------------------------
# part_two()
# Execute the jumps in the given code including that we either
# increase or decrease the offset in each jump instruction
# that we executed.
#
# Exit the code when the jump ends up outside of the code.
# Print how many cycles it took.
#-------------------------------------------------------------------
def part_two(code):
    print("Part two:")
    ctr = 0
    pc = 0
    codelen = len(code)
    offset = 0

    while pc >= 0 and pc < codelen:
        offset = code[pc]
        print("pc = %d, offset = %d" % (pc, offset))

        if offset >= 3:
            code[pc] = code[pc] - 1
        else:
            code[pc] = code[pc] + 1

        pc = pc + offset
        ctr += 1

    print("Exited code at pc = %d after %d cycles." % (pc, ctr))
    print()
    return (code, ctr)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def test_two():
    code = [0, 3, 0, 1, -3]
    ref = ([2, 3, 2, 3, -1], 10)

    print("test code for part two:")
    print("code before execution:")
    print(code)
    code2 = part_two(code)
    print("code after execution:")
    print(code2)

    if code2 == ref:
        print("Correct result after execution.")


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    test_two()
#    my_code = get_input()
#    part_one(my_code)
#    part_two(my_code)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_5.py
#=======================================================================
