
def score(node_a, node_b):
    tags_a = node_a['tags']
    tags_b = node_b['tags']
    common_tags = len(list(set(tags_a + tags_b)))
    unique_a = len(list(set(tags_a) - set(tags_b)))
    unique_b = len(list(set(tags_b) - set(tags_a)))
    return min(common_tags, unique_a, unique_b)
