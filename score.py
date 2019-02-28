
def getScore(node_a, node_b):
    tags_a = node_a.v_tags_1 + node_a.v_tags_2 + node_a.h_tags
    tags_b = node_b.v_tags_1 + node_b.v_tags_2 + node_b.h_tags
    common_tags = len(set(tags_a + tags_b))
    unique_a = len(set(tags_a) - set(tags_b))
    unique_b = len(set(tags_b) - set(tags_a))
    return min(common_tags, unique_a, unique_b)
