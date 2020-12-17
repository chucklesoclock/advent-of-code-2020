import itertools

with open("input/data09.txt") as f:
    data = [int(x) for x in f.readlines()]

preamble = 25


def part1(data=data, preamble=preamble):
    for i in range(preamble, len(data)):
        window = data[i - preamble : i]
        n = data[i]
        # recalculating all the sums is inefficient
        # i should only have to drop and add n=preamble-1 sums
        if n not in (sum(tup) for tup in itertools.combinations(window, 2)):
            return n
    else:
        raise Exception("all numbers are sum of 2 numbers in preamble")


def part2(target, data=data):
    for i in range(len(data) - 1):
        window_sum = data[i]
        if window_sum > target:
            continue
        for j in range(i+1, len(data)):
            window_sum += data[j]
            if window_sum == target:
                winning_window = data[i : j + 1]
                return min(winning_window) + max(winning_window)
            elif window_sum > target:
                break
        else:
            assert window_sum < target
    else:
        return None


if __name__ == "__main__":
    first_invalid = part1()
    print(first_invalid)
    print(part2(first_invalid))

sample_input = [
    int(x)
    for x in """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()
]


def test_sample_part_1():
    assert part1(sample_input, 5) == 127


def test_sample_part_2():
    assert part2(127, sample_input) == 62