#!/usr/bin/python3

import sys


def nacci(n, count):
    seq = [0] * (n - 1) + [1]
    for i in range(count):
        seq.append(sum(seq[-n:]))
    return seq[n-2:]


def format_seq(seq):
    for el in seq:
        print(f"& {el} ", end="")
    print()


format_seq(nacci(int(sys.argv[1]), int(sys.argv[2])))
