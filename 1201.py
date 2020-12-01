
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


def two_to_2020():
    numbers = read_input()
    final_value = None
    for number in numbers:
        for x in range(1, len(numbers)):
            if(number + numbers[x] == 2020):
                final_value = number * numbers[x]
    
    print("Final Value: %d" % final_value)


def three_to_2020():
    numbers = read_input()
    final_value = None
    for number in numbers:
        for x in range(1, len(numbers)):
            for y in range(2, len(numbers)):
                if(number + numbers[x] + numbers[y] == 2020):
                    final_value = number * numbers[x] * numbers[y]
    
    print("Final Value: %d" % final_value)


def main():
    print("Two that produce 2020")
    two_to_2020()
    print("Three that produce 2020")
    three_to_2020()

main()