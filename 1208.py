def read_input():
    with open('12_08_input.txt') as reader:
        return [line.strip() for line in reader]


def visit_no_repeats(insts):
    prev_inst = []
    acc = 0
    idx = 0

    while idx not in prev_inst:
        prev_inst.append(idx)
        inst = insts[idx]
        inst_split = inst.split(' ')

        oper = inst_split[0]
        val = inst_split[1]

        value = int(val[1:]) if val.startswith('+') else int(val)
        if oper == 'acc':
            acc += value
            prev_inst.append(idx)
            idx+=1
        elif oper == 'jmp':
            prev_inst.append(idx)
            idx += value
        elif oper == 'nop':
            prev_inst.append(idx)
            idx+=1

        if idx == len(insts):
            return acc, True

    return acc, False


def main():
    insts = read_input()

    acc_part_1, eol = visit_no_repeats(insts)

    print("Part 1: %d" % acc_part_1)

    done = False
    idx = 0
    while not done:
        temp_inst = list(insts)

        if temp_inst[idx].startswith('jmp'):
            temp_inst[idx] = "nop" + temp_inst[idx][3:]
        elif temp_inst[idx].startswith('nop'):
            temp_inst[idx] = "jmp" + temp_inst[idx][3:]
        acc_part_2, eol = visit_no_repeats(temp_inst)
        if eol:
            done = True

        idx += 1

    print("Part 2: %d" % acc_part_2)


if __name__ == '__main__':
    main()
