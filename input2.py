def input(filename):
    all_tags = []
    vert = {}
    hor = {}
    f = open(filename).readlines()
    for i, line in enumerate(f[1:]):
        stuff = line.split()
        for tag in stuff[2:]:
            if not tag in all_tags:
                all_tags.append(tag)
        if (stuff[0] == "H"):
            hor[i] = list(map(lambda x: all_tags.index(x), stuff[2:]))
        else:
            vert[i] = list(map(lambda x: all_tags.index(x), stuff[2:]))
    return(vert, hor)

