
def getScore(node_a, node_b):
    common_tags = len(set(node_a.all_tags + node_b.all_tags))
    unique_a = len(set(node_a.all_tags) - set(node_b.all_tags))
    unique_b = len(set(node_b.all_tags) - set(node_a.all_tags))
    return min([common_tags, unique_a, unique_b])

def scoreArray(slides):
    score = 0
    slides_count = len(slides)
    for i, s in enumerate(slides):
        if i + 1 < slides_count:
            score += getScore(s, slides[i + 1])

    return score
