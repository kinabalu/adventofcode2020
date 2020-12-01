def read_input():
    numbers = []
    with open('12_01_input.txt') as reader:
        lines = reader.readlines()

        for line in lines:
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                print("Input contained non-int data")
                process.exit(1)
    return numbers


def calculate():
    numbers = read_input()
    final_value = None
    final_value_3 = None
    for number in numbers:
        for x in range(1, len(numbers)):
            if(number + numbers[x] == 2020):
                final_value = number * numbers[x]
            for y in range(2, len(numbers)):
                if(number + numbers[x] + numbers[y] == 2020):
                    final_value_3 = number * numbers[x] * numbers[y]

    return final_value, final_value_3

def main():
    final_value, final_value_3 = calculate()
    print("Two that produce 2020")
    print(final_value)
    print("Three that produce 2020")
    print(final_value_3)

if __name__ == '__main__':
    main()