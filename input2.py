def input(filename):
    all_tags = []
    vert = {}
    hor = {}
    f = open(filename).readlines()
    pics = []
    for i, line in enumerate(f[1:]):
        stuff = line.split()
        o = stuff[0]
        for tag in stuff[2:]:
            if not tag in all_tags:
                all_tags.append(tag)
        if (o == "H"):
            hor[i] = list(map(lambda x: all_tags.index(x), stuff[2:]))
        else:
            vert[i] = list(map(lambda x: all_tags.index(x), stuff[2:]))
    return(vert, hor)

