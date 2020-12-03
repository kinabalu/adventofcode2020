from operator import itemgetter


def read_input():
    rules_with_data = []
    with open('12_02_input.txt') as reader:
        lines = reader.readlines()

        for line in lines:
            elements = line.split(' ')
            iterations_of_char = elements[0]
            char = elements[1][0]
            data = elements[2].strip()

            try:
                iteration_elements = iterations_of_char.split('-')
                first_int = int(iteration_elements[0])
                second_int = int(iteration_elements[1])
            except ValueError:
                print("Iterations of char input contained non-int data")
                process.exit(1)

            rules_with_data.append({
                'first_int': first_int,
                'second_int': second_int,
                'char': char,
                'data': data
            })
    return rules_with_data


def sled_rental_valid_password(rule_with_data):

    char_iteration = 0
    for character in rule_with_data['data']:
        if character == rule_with_data['char']:
            char_iteration+=1

    if rule_with_data['first_int'] <= char_iteration <= rule_with_data['second_int']:
        return True

    return False


def char_at_index(char, data, idx):
    try:
        return data[idx-1] == char
    except IndexError:
        return False


def toboggan_valid_password(rule_with_data):

    char, data, first_int, second_int = itemgetter('char', 'data', 'first_int', 'second_int')(rule_with_data)

    found_at_first_pos = char_at_index(char, data, first_int)
    found_at_second_pos = char_at_index(char, data, second_int)

    return found_at_first_pos != found_at_second_pos


def main():
    data_rules = read_input()

    sled_rental_valid_password_count = 0
    toboggan_valid_password_count = 0
    for data_rule in data_rules:
        sled_rental_valid_password_count += 1 if sled_rental_valid_password(data_rule) else 0
        toboggan_valid_password_count += 1 if toboggan_valid_password(data_rule) else 0

    print("Sled rental place valid passwords in input file: %d" % sled_rental_valid_password_count)
    print("Toboggan place valid passwords in input file: %d" % toboggan_valid_password_count)


if __name__ == '__main__':
    main()