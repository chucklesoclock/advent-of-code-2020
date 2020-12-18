from collections import Counter


def parse(data):
    return [int(x) for x in data.splitlines()]


def part1(data):
    differences = Counter()
    data.sort()
    for i in range(len(data)):
        joltage = data[i]
        diff = joltage if i == 0 else joltage - data[i - 1]
        differences[diff] += 1
    else:
        # device adapter always +3
        differences[3] += 1
    return differences[1] * differences[3]


if __name__ == "__main__":
    with open("input/data10.txt") as f:
        data = parse(f.read())
    print(part1(data))

sample_1 = parse(
    """16
10
15
5
1
11
7
19
6
12
4"""
)

sample_2 = parse(
    """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
)


def test_sample_1():
    assert part1(sample_1) == 7 * 5


def test_sample_2():
    assert part1(sample_2) == 22 * 10
