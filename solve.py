class Solver:

    def __init__(self, filename):
        self.in_file = filename
        self.out_file = "outputs/" + filename.split('/')[1]

        self.slides = []

        self.photos, self.h, self.v = self.input()

    def score(self, photo1, photo2):
        s1 = self.photos[photo1][1]
        s2 = self.photos[photo2][1]
        return min(len(s1 & s2), len(s1 - s2), len(s2 - s1))

    def solve(self):
        print(self.score(0, 3))

    def input(self):

        with open(self.in_file) as f:
            P = int(f.readline())
            tags = {}
            tag_id = 0
            photos = []
            h = []
            v = []
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

                horizontal = O == 'H'
                photos.append((horizontal, set(tag_ids)))
                if horizontal:
                    h.append(i)
                else:
                    v.append(i)

        return (photos, h, v)

    def output(self):
        with open(self.out_file, "w") as f:
            f.write("%d" % len(self.slides))
            for slide in self.slides:
                if len(slide) > 0:
                    f.write("%d", slide)
                else:
                    f.write("%d %d", (slide[0], slide[1]))


solver = Solver("inputs/a_example.txt")
solver.solve()
solver.output()
