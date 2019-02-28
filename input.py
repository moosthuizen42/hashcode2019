import numpy as np


def read_input(filename):

    lines = open(filename).readlines()

    P = int(lines[0])

    # tags = []
    v = []
    h = []

    for i, row in enumerate(lines[1:]):
        elements = row.strip().split(' ')
        O = elements[0]
        T = elements[2:]

        if O == 'H':
            h.append({"id": i, "tags": T})
        else:
            v.append({"id": i, "tags": T})

    return P, v, h


# P, v, h = read_input("inputs/a_example.txt")
