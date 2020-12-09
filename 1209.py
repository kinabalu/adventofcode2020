def read_input():
    with open('12_09_input.txt') as reader:
        return [int(line.strip()) for line in reader]


def main():
    data = read_input()

    prev_25 = []
    idx = 0
    found = False
    xmas_number = None

    while idx < len(data) and not found:
        entry = data[idx]

        if idx > 25:
            test_found = False
            for x in range(0, 25):
                for y in range(1, 25):
                    if entry == prev_25[x] + prev_25[y]:
                        test_found = True
                        break
            if not test_found:
                xmas_number = entry
                found = True

        if len(prev_25) == 25:
            prev_25.pop(0)
        prev_25.append(entry)
        idx+=1

    add_set = []
    contiguous_found = False
    contiguous_add = None
    x = 0

    while not contiguous_found and x in range(0, len(data)):
        total = data[x]
        add_set.append(data[x])

        x += 1
        y = 1
        while not contiguous_found and y in range(1, len(data)):
            total += data[y]
            add_set.append(data[y])
            y += 1

            if total == xmas_number and len(add_set) > 1:
                add_set.sort()

                contiguous_add = add_set[0] + add_set[len(add_set) - 1]
                contiguous_found = True
                break
            elif total > xmas_number:
                add_set = []
                total = 0

    print("part 1: %d" % xmas_number)
    print("part 2: %d" % contiguous_add)


if __name__ == '__main__':
    main()
