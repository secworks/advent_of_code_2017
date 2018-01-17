#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day_18.py
# --------
# Solution for Advent of code 2017, day 18.
# https://adventofcode.com/2017/day/18
#
#
# Status: Not done.
#
# Joachim Strömbergson 2018
#
#=======================================================================

import sys

VERBOSE = 0


#-------------------------------------------------------------------
# load_sw()
#
# Load the dance from file, parsing the moves into something
# we can easily perform.
#-------------------------------------------------------------------
def load_sw():
    program = []
    if VERBOSE:
        print("Loading program...")

    with open('my_input.txt','r') as f:
        for line in f:
            line = line.rstrip()
            program.append(line.split(' '))
    return program


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def build_regfile(sw):
    regfile = {}
    for instr in sw:
        if len(instr) == 3:
            (opcode, reg, value) = instr
        else:
            (opcode, reg) = instr
        if reg.isalpha():
            regfile[reg] = 0
    return regfile


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def execute(regs, prg):
    pc = 0
    ctr = 0
    end = len(prg)
    while (pc > 0) and (pc <= end):
        instr = prg[pc]

        if len(instr) = 3:
            (op, reg, mod) = instr
        else:
            (op, reg) = instr

        if op == "set":
            regs[reg] = mod
            pc += 1

        if op == "mul":
            regs[reg] = regs[reg] * mod
            pc += 1

        if op == "jgz":
            pass


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_program = load_sw()
    my_regfile = build_regfile(my_program)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day18.py
#=======================================================================
