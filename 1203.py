def read_input():
    forest = []
    with open('12_03_input.txt') as reader:
        lines = reader.readlines()

        for line in lines:
            row = []
            for pos in line.strip():
                row.append(pos)

            forest.append(row)
    return forest


def crawl(forest, right, down):
    x = 0

    tree_count = 0
    for row in range(down, len(forest), down):
        x = x + right if x + right < len(forest[row]) else x + right - len(forest[row])
        tree_count += 1 if forest[row][x] == '#' else 0

    return tree_count


def main():
    """
    - Right 1, down 1
    - Right 3, down 1 -- original step 1
    - Right 5, down 1
    - Right 7, down 1
    - Right 1, down 2
    """
    forest = read_input()

    multiplied = crawl(forest, 1, 1) * crawl(forest, 3, 1) * crawl(forest, 5, 1) * crawl(forest, 7, 1) * crawl(forest, 1, 2)
    print("Tree count (3, 1): %d" % crawl(forest, 3, 1))
    print("Tree count multiplied: %d" % multiplied)


if __name__ == '__main__':
    main()