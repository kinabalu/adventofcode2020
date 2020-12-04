def read_input():
    with open('12_04_input.txt') as reader:
        input_text = reader.read()
        passports = input_text.split('\n\n')

        return passports


def has_all_required_values(str, required):
    return all(s in str for s in required)


def has_any_required_values(str, required):
    return any(s in str for s in required)


def is_range_valid(str, min, max):
    try:
        num = int(str)

        return min <= num <= max
    except ValueError:
        return False


def is_size_valid(str, size):
    try:
        int(str)
        return len(str) == size
    except ValueError:
        return False


def is_valid_record(passport_record, required, extra_validation=True):
    required_fields = has_all_required_values(passport_record, required)

    if not required_fields:
        return False

    if extra_validation:
        kv = dict(s.split(':')  for s in [f.strip() for f in passport_record.split()])

        if not is_range_valid(kv['byr'], 1920, 2002):
            return False

        if not is_range_valid(kv['iyr'], 2010, 2020):
            return False

        if not is_range_valid(kv['eyr'], 2020, 2030):
            return False

        hgt_val = kv['hgt'][:-2]
        if kv['hgt'].endswith('cm'):
            if not is_range_valid(hgt_val, 150, 193):
                return False
        elif kv['hgt'].endswith('in'):
            if not is_range_valid(hgt_val, 59, 76):
                return False
        else:
            return False

        if not kv['hcl'][0] == '#' or not kv['hcl'][1:].isalnum() or len(kv['hcl'][1:]) != 6:
            return False

        if not has_any_required_values(kv['ecl'], ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            return False

        if not is_size_valid(kv['pid'], 9):
            return False

    return True


def main():
    passports = read_input()

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passport_count = 0
    valid_passport_validation_count = 0

    for passport_record in passports:
        valid_passport_count += 1 if is_valid_record(passport_record, required_fields, False) else 0
        valid_passport_validation_count += 1 if is_valid_record(passport_record, required_fields) else 0

    print("Number of passports: %d" % len(passports))
    print("Number of valid passports: %d" % valid_passport_count)
    print("Number of valid passports+validation: %d" % valid_passport_validation_count)


if __name__ == '__main__':
    main()