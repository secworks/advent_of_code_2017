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
    print("here!")
    sound   = 0
    receive = 0
    pc = 0
    ctr = 0
    end = len(prg)
    while (pc >= 0) and (pc <= end):
        # Get next instruction, extract opcodes, regs and modifiers.
        # Handle different instruction formats during extraction.
        instr = prg[pc]
        print("Executing instruction:", instr)
        if len(instr) == 3:
            (op, reg, mod) = instr
        else:
            (op, reg) = instr

        # Parse and execute each operation including variants.
        if op == "add":
            pc += 1
            if mod.isalpha():
                regs[reg] = regs[reg] + regs[mod]
            else:
                regs[reg] = regs[reg] + int(mod)

        if op == "jgz":
            if reg.isalpha():
                cond = regs[reg]
            else:
                cond = int(reg)
            if cond > 0:
                if mod.isalpha():
                    pc = pc + regs[mod]
                else:
                    pc = pc + int(mod)

        if op == "mod":
            pc += 1
            if mod.isalpha():
                regs[reg] = regs[reg] % regs[mod]
            else:
                regs[reg] = regs[reg] % int(mod)

        if op == "mul":
            pc += 1
            regs[reg] = regs[reg] * int(mod)

        if op == "rcv":
            pc += 1
            if regs[reg] != 0:
                receive = sound
                print("receive set to %d" % (receive))

        if op == "set":
            pc += 1
            regs[reg] = int(mod)

        if op == "snd":
            pc += 1
            sound = regs[reg]


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    my_program = load_sw()
    my_regfile = build_regfile(my_program)
    execute(my_regfile, my_program)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day18.py
#=======================================================================
