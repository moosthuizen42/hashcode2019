from score import score

def main():
    node_a = {
        "tags": ['test', 'cat', 'dog']
    }
    node_b = {
        "tags": ['test', 'pizza', 'home', 'beer']
    }

    print(score(node_a, node_b))

if __name__ == '__main__':
    main()
