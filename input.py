import numpy as np


def read_input(filename):

    lines = open(filename).readlines()

    P = int(lines[0])

    tags = {}

    verticals = []
    horizontals = []

    for row in lines[1:]:
        elements = row.strip().split(' ')
        O = elements[0]
        T = elements[2:]

        if O == 'H':
            horizontals.append(T)
        else:
            verticals.append(T)

    return P, verticals, horizontals


P, v, h = read_input("inputs/a_example.txt")
