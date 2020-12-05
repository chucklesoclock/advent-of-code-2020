from timethis import timethis


def yield_entries(data):
    for entry in data:
        a, b = map(int, entry[0].split('-'))
        keychar = entry[1].rstrip(':')
        password = entry[2]
        yield a, b, keychar, password


def part1(data):
    n_valid = 0
    for low, hi, keychar, password in yield_entries(data):
        n = password.count(keychar)
        if n < low or n > hi:
            continue
        else:
            n_valid += 1
    return n_valid


def part2(data):
    n_valid = 0
    for a, b, keychar, password in yield_entries(data):
        try:
            if (password[a-1] == keychar) ^ (password[b-1] == keychar):
                n_valid += 1
        except IndexError:
            continue
    return n_valid


@timethis
def main():
    with open('data.txt') as f:
        data = [x.split() for x in f.readlines()]
        print(part1(data))
        print(part2(data))


if __name__ == "__main__":
    main()
