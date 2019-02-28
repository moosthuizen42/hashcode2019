from score import getScore

def main():
    node_a = {
        "tags": ['test', 'cat', 'dog']
    }
    node_b = {
        "tags": ['test', 'pizza', 'home', 'beer']
    }

    print(getScore(node_a, node_b))

if __name__ == '__main__':
    main()
