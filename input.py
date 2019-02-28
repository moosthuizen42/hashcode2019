import numpy as np
from slide import Slide


def read_input(filename):

    lines = open(filename).readlines()

    P = int(lines[0])

    tags = []
    v = []
    h = []

    for i, row in enumerate(lines[1:]):
        elements = row.strip().split(' ')
        O = elements[0]
        T = elements[2:]

        if O == 'H':
            h.append(Slide(h_tags=T, h_image=i))
        else:
            v.append(Slide(v_tags_1=T, v_image_1=i))

    return P, v, h


def write_output(filename, slides):

    with open(filename, "w") as f:
        f.write("%d" % len(self.slides))
        # for slide in self.slides:
        #     if len(slide) > 0:
        #         f.write("%d", slide)
        #     else:
        #         f.write("%d %d", (slide[0], slide[1]))


# P, v, h = read_input("inputs/a_example.txt")
