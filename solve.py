from input import read_input


class Solver:

    def __init__(self, filename):
        self.in_file = filename
        self.out_file = "outputs/" + filename.split('/')[1]

        self.photos = []
        self.slides = []

        self.input()

    def input(self):

        with open(self.in_file) as f:
            P = int(f.readline())
            tags = {}
            tag_id = 0
            v = {}
            h = {}
            for i, line in enumerate(f):
                items = line.strip().split(' ')
                O = items[0]
                T = items[2:]
                tag_ids = []
                for tag in T:
                    if not tag in tags.keys():
                        tags[tag] = tag_id
                        tag_id += 1
                    tag_ids.append(tags[tag])
                if O == 'h':
                    h[i] = tag_ids
                else:
                    v[i] = tag_ids

        return None

        # lines = open(filename).readlines()

        # for i, row in enumerate(lines[1:]):
        # elements = row.strip().split(' ')
        # O = elements[0]
        # T = elements[2:]

        # if O == 'H':
        #     h.append({"id": i, "orientation": O, "tags": T})
        # else:
        #     v.append({"id": i, "orientation": O, "tags": T})

    def output(self):
        with open(self.out_file, "w") as f:
            f.write("%d" % len(self.slides))
            for slide in self.slides:
                if len(slide) > 0:
                    f.write("%d", slide)
                else:
                    f.write("%d %d", (slide[0], slide[1]))


solve = Solver("inputs/a_example.txt")

solve.output()
