import math


def read_input():
    with open('12_05_input.txt') as reader:
        return [line.strip() for line in reader]


def split(min, max, space):
    if space == 'F' or space == 'L':
        return min, (math.floor((max - min) / 2)) + min
    elif space == 'B' or space == 'R':
        return math.floor(((((max - min) + 1) / 2) + min)), max


def generate_seat_id(row, col):
    return (row * 8) + col


def main():
    partitions = read_input()

    seat_ids = []
    highest_seat_id = None
    for partition in partitions:
        row_min = 0
        row_max = 127
        row = None
        for row_idx in range(0, 7):
            row_min, row_max = split(row_min, row_max, partition[row_idx])

        if row_min == row_max:
            row = int(row_min)

        col_min = 0
        col_max = 7
        col = None
        for col_idx in range(7, 10):
            col_min, col_max = split(col_min, col_max, partition[col_idx])

        if col_min == col_max:
            col = int(col_min)

        new_seat_id = generate_seat_id(row, col)
        seat_ids.append(new_seat_id)
        highest_seat_id = new_seat_id if new_seat_id > highest_seat_id else highest_seat_id

    seat_ids.sort()

    print("Highest seat id is %d" % highest_seat_id)
    print("Missing seat is %d" % [x for x in range(seat_ids[0], seat_ids[-1]+1) if x not in seat_ids][0])


if __name__ == '__main__':
    main()