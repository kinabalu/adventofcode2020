from functools import reduce
import operator


def read_input():
    with open('12_03_input.txt') as reader:
        forest = [line.strip() for line in reader]
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

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    multiplied = reduce(operator.mul, [crawl(forest, *slope) for slope in slopes])

    print("Tree count (3, 1): %d" % crawl(forest, 3, 1))
    print("Tree count multiplied: %d" % multiplied)


if __name__ == '__main__':
    main()