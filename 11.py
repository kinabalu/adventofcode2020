with open('./data/2020/11-sample.txt') as reader:
    data = [line.split() for line in reader]


def get_seat(matrix, row, col):
    if row == -1 or col == -1:
        return None
    try:
        return matrix[row][0][col]
    except IndexError:
        return None


def adjacent_seat(matrix, row, col, continuous=False):
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    aos = 0

    for i in dir:
        if continuous:
            x = 0
            while True:
                row_i = i[0]
                col_i = i[1]
                for times in range(x):
                    row_i += i[0]
                    col_i += i[1]
                adj_seat = get_seat(matrix, row_i, col_i)
                if adj_seat == '#':
                    aos += 1
                elif adj_seat is None:
                    break
                x+=1
        else:
            adj_seat = get_seat(matrix, row + i[0], col + i[1])
            if adj_seat == '#':
                aos += 1
    return aos


def occupied_game(d, seat_tolerance=4, continuous=False):
    new_data = []
    data_change = False

    occupied = 0
    for x in range(0, len(d)):
        row = ""
        for y in range(0, len(d[x][0])):
            adj_seat_count = adjacent_seat(d, x, y, continuous=continuous)

            current_seat = d[x][0][y]

            if adj_seat_count == 0 and current_seat == 'L':
                row += '#'
                occupied += 1
                data_change = True
            elif adj_seat_count >= seat_tolerance and current_seat == '#':
                row += 'L'
                data_change = True
            elif current_seat == '.':
                row += '.'
            else:
                if current_seat == '#':
                    occupied += 1
                row += current_seat

        #     print(data_change, current_seat, adj_seat_count, x, y, occupied)
        #
        # print()
        new_data.append([row])

    # print("========================================")
    # import pprint
    # pprint.pprint(new_data)

    if data_change:
        return occupied_game(new_data)
    else:
        return occupied


occupied = occupied_game(data, seat_tolerance=4)
print("part 1-%d" % occupied)

occupied_2 = occupied_game(data, seat_tolerance=5, continuous=True)
print("part 2-%d" % occupied_2)