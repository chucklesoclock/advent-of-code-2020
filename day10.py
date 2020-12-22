from collections import Counter
from scipy.sparse import coo_matrix
import numpy as np


def parse(data):
    return sorted([int(x) for x in data.splitlines()])


def part1(data):
    differences = Counter()
    for i in range(len(data)):
        joltage = data[i]
        diff = joltage if i == 0 else joltage - data[i - 1]
        differences[diff] += 1
    else:
        # device adapter always +3
        differences[3] += 1
    return differences[1] * differences[3]


def part2(data):
    adj_size_nxn = len(data) + 2
    last_adapter_i = adj_size_nxn - 2
    device_j = adj_size_nxn - 1

    def build_adjacency_matrix(data):
        adj_matrix = np.zeros((adj_size_nxn, adj_size_nxn), dtype="int64")
        enhanced_data = [0] + data
        for i, x in enumerate(enhanced_data):
            j = i + 1
            try:
                while enhanced_data[j] - x < 4 and j - i < 4:
                    adj_matrix[i, j] = 1
                    j += 1
            except IndexError:
                continue
        else:
            adj_matrix[last_adapter_i, device_j] = 1
        return adj_matrix

    m = build_adjacency_matrix(data)
    outlet_to_device = (0, device_j)

    n = 2
    num_paths = 0
    acc = m
    # max number of paths is len(data) + 1
    while n < adj_size_nxn:
        acc = np.matmul(acc, m)
        num_paths += acc[outlet_to_device]
        n += 1
    return num_paths

if __name__ == "__main__":
    with open("input/data10.txt") as f:
        data = parse(f.read())
    print(part1(data))
    print(part2(data))

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


def test_part_1_sample_1():
    assert part1(sample_1) == 7 * 5


def test_part_1_sample_2():
    assert part1(sample_2) == 22 * 10


def test_part_2_sample_1():
    assert part2(sample_1) == 8


def test_part_2_sample_2():
    assert part2(sample_2) == 19208