with open('./data/2020/10.txt') as reader:
    data = [int(line.strip()) for line in reader]

one_jolt_count, three_jolt_count = 0, 0

data.append(0)              # initial outlet counts
data.sort()
data.append(max(data)+3)    # max + 3 for the last jolt

for x in range(len(data) - 1):
    next = data[x+1] - data[x]
    if next == 1:
        one_jolt_count += 1
    elif next == 3:
        three_jolt_count += 1

print(one_jolt_count*three_jolt_count)

count = len(data)

d = [0] * count
d[0] = 1

for outer in range(1, count):
    for inner in range(outer):
        if data[outer] - data[inner] <= 3:
            d[outer] += d[inner]

print(d[count - 1])