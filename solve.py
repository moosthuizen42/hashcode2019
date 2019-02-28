class Solver:

    def __init__(self, filename):
        self.in_file = filename
        self.out_file = "outputs/" + filename.split('/')[1]

        self.slides = []

        self.photos, self.h, self.v = self.input()

    def score(self, slide1, slide2):
        if not isinstance(slide1, list):
            s1 = self.photos[slide1][1]
        else:
            s1 = self.photos[slide1[0]][1] | self.photos[slide1[1]][1]

        if not isinstance(slide2, list):
            s2 = self.photos[slide2][1]
        else:
            s2 = self.photos[slide2[0]][1] | self.photos[slide2[1]][1]

        return min(len(s1 & s2), len(s1 - s2), len(s2 - s1))

    def solve(self):

        self.slides.append(self.h.pop())
        H = len(self.h)

        total = 0

        while H > 0:

            for h in range(H):
                score = self.score(self.slides[-1], self.h[h])
                total += score
                if score > 0:
                    self.slides.append(self.h[h])
                    del self.h[h]
                    break

            H = len(self.h)
            print((H, total))

            # V = len(self.v)

            # while H + V > 0:

            #     if H > 0:
            #         self.slides.append(self.h.pop())

            #     if V > 0:
            #         self.slides.append([self.v.pop(), self.v.pop()])

            #     H = len(self.h)
            #     V = len(self.v)

    def validate(self):
        pass

    def total_score(self):

        score = 0
        for i in range(len(self.slides) - 1):
            slide1 = self.slides[i]
            slide2 = self.slides[i + 1]
            score += self.score(slide1, slide2)

        return score

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
            f.write("%d\n" % len(self.slides))
            for slide in self.slides:
                if not isinstance(slide, list):
                    f.write("%d\n" % slide)
                else:
                    f.write("%d %d\n" % (slide[0], slide[1]))


# solver = Solver("inputs/a_example.txt")
solver = Solver("inputs/b_lovely_landscapes.txt")
# solver = Solver("inputs/c_memorable_moments.txt")
# solver = Solver("inputs/d_pet_pictures.txt")
# solver = Solver("inputs/e_shiny_selfies.txt")

solver.solve()
print(solver.total_score())
solver.output()
