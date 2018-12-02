#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_8.py
# --------
# Solution for Advent of code 2017, day 8.
# http://adventofcode.com/2017/day/8
#
# Status: Done.
#
# Joachim Strömbergson 2017
#
#=======================================================================

import sys

VERBOSE = 1


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input():
    instr = []
    with open('my_input.txt','r') as f:
        for line in f:
            instr.append(line.split())
    return instr


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_regs(instructions):
    regs = {}
    for instr in instructions:
        (destreg, mod, modop, ifw, condreg, cond, condval) = instr
        regs[destreg] = 0
        regs[condreg] = 0
    return regs


#-------------------------------------------------------------------
# execute()
#
# Execute the given instruction, using, updating the registers.
# First check if the condition is true or not.
# If condition is true execute the modification.
#-------------------------------------------------------------------
def execute(instr, regs):
    (destreg, mod, modop, ifw, condreg, cond, condval) = instr
    do_modop = False

    if cond == "==":
        if regs[condreg] == int(condval):
            do_modop = True
    if cond == "!=":
        if regs[condreg] != int(condval):
            do_modop = True
    if cond == ">":
        if regs[condreg] > int(condval):
            do_modop = True
    if cond == ">=":
        if regs[condreg] >= int(condval):
            do_modop = True
    if cond == "<":
        if regs[condreg] < int(condval):
            do_modop = True
    if cond == "<=":
        if regs[condreg] <= int(condval):
            do_modop = True

    if do_modop:
        if mod == "inc":
            regs[destreg] += int(modop)
        if mod == "dec":
            regs[destreg] -= int(modop)

    return regs

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_max(regs):
    maxval = -100000000
    for i in regs.values():
        if i > maxval:
            maxval = i
    return maxval

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def main():
    my_instructions = get_input()
    my_regs = get_regs(my_instructions)

    endmax = -100000000
    procmax = -100000000

    for instr in my_instructions:
        my_regs = execute(instr, my_regs)
        if get_max(my_regs) > procmax:
            procmax = get_max(my_regs)

    endmax = get_max(my_regs)

    print("Max value in reg during processing: %d" % procmax)
    print("Max value in reg after processing: %d" % endmax)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day_8.py
#=======================================================================
