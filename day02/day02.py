from timethis import timethis


def check_valid_part1(low, hi, keychar, password):
    n = password.count(keychar)
    if n < low or n > hi:
        return False
    else:
        return True


def check_valid_part2(a, b, keychar, password):
    try:
        if (password[a-1] == keychar) ^ (password[b-1] == keychar):
            return True
        else:
            return False
    except IndexError:
        return False


def process_line(line):
    entry = line.split()
    a, b = map(int, entry[0].split('-'))
    keychar = entry[1].rstrip(':')
    password = entry[2]
    return a, b, keychar, password


@timethis
def main():
    with open('data.txt') as f:
        n_valid_part_1 = n_valid_part_2 = 0
        for line in f:
            a, b, keychar, password = process_line(line)
            if check_valid_part1(a, b, keychar, password):
                n_valid_part_1 += 1
            if check_valid_part2(a, b, keychar, password):
                n_valid_part_2 += 1
    print(n_valid_part_1)
    print(n_valid_part_2)


if __name__ == "__main__":
    main()
