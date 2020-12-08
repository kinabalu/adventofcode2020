def read_input():
    with open('12_06_input.txt') as reader:
        input_text = reader.read()
        answers = input_text.split('\n\n')

        return answers


def main():
    answers = read_input()

    part1, part2 = 0, 0

    for answer in answers:
        letters = {}
        entries = answer.split('\n')

        for entry in entries:
            for letter in entry:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1

        for letter in letters:
            occurrence = letters[letter]
            part2 += 1 if occurrence == len(entries) else 0

        answer = answer.replace("\n", "")
        unique_set = ''.join(set(answer))
        part1 += len(unique_set)

    print("Part 1-%d\nPart 2-%d" % (part1, part2))


if __name__ == '__main__':
    main()