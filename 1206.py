def read_input():
    with open('12_06_input.txt') as reader:
        input_text = reader.read()
        answers = input_text.split('\n\n')

        return answers


def main():
    answers = read_input()

    part1_answer_count = 0
    part2_answer_count = 0
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
            part2_answer_count += 1 if occurrence == len(entries) else 0

        answer = answer.replace("\n", "")
        unique_set = ''.join(set(answer))
        part1_answer_count += len(unique_set)

    print("Part 1-%d\nPart 2-%d" % (part1_answer_count, part2_answer_count))


if __name__ == '__main__':
    main()