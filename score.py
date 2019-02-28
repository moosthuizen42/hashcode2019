
def getScore(node_a, node_b):
    tags_a = node_a.v_tags_1 + node_a.v_tags_2 + node_a.h_tags
    tags_b = node_b.v_tags_1 + node_b.v_tags_2 + node_b.h_tags
    common_tags = len(set(tags_a + tags_b))
    unique_a = len(set(tags_a) - set(tags_b))
    unique_b = len(set(tags_b) - set(tags_a))
    return min(common_tags, unique_a, unique_b)

def scoreArray(slides):
    score = 0
    slides_count = len(slides)
    for i, s in enumerate(slides):
        if i + 1 < slides_count:
            score += getScore(s, slides[i + 1])
