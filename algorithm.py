from input import read_input


class Algorithm:

    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.used_v = []
        self.slides = []


P, v, h = read_input("inputs/a_example.txt")
alg = Algorithm(v, h)
