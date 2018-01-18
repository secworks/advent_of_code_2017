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
    sound   = 0
    receive = 0
    pc = 0
    ctr = 0
    end = len(prg)
    while (pc >= 0) and (pc <= end) and ctr < 100000:
        ctr += 1
        # Get next instruction, extract opcodes, regs and modifiers.
        # Handle different instruction formats during extraction.
        instr = prg[pc]

        print("Ctr: %d, PC: %d. Executing instruction:" % (ctr, pc), instr)

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
            else:
                pc += 1


        if op == "mod":
            pc += 1
            if mod.isalpha():
                regs[reg] = regs[reg] % regs[mod]
            else:
                regs[reg] = regs[reg] % int(mod)


        if op == "mul":
            pc += 1
            if mod.isalpha():
                regs[reg] = regs[reg] * regs[mod]
            else:
                regs[reg] = regs[reg] * int(mod)


        if op == "rcv":
            pc += 1
            if regs[reg] != 0:
                receive = sound
                print("receive set to %d" % (receive))


        if op == "set":
            pc += 1
            if mod.isalpha():
                regs[reg] = regs[mod]
            else:
                regs[reg] = int(mod)


        if op == "snd":
            pc += 1
            sound = regs[reg]


        # Dump the state:
        print("Current state: ", regs)
        print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def testcase():
    test_program = [['set', 'a', '1'], ['add', 'a', '2'], ['mul', 'a', 'a'],
                    ['mod', 'a', '5'], ['snd', 'a'], ['set', 'a', '0'],
                    ['rcv', 'a'], ['jgz', 'a', '-1'], ['set', 'a',  '1'],
                    ['jgz', 'a',  '-2']]

    test_regfile = build_regfile(test_program)
    execute(test_regfile, test_program)


#-------------------------------------------------------------------
# main()
#-------------------------------------------------------------------
def main():
    testcase()
#    my_program = load_sw()
#    my_regfile = build_regfile(my_program)
#    execute(my_regfile, my_program)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF day18.py
#=======================================================================
