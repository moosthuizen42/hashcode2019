def output(labels):
    f = open("output.txt", "w")
    f.write(f"{len(labels)}\n")
    for i in labels:
        f.write(f"{i}\n")
    f.close()
