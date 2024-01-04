import pytest
import numpy as np


def parse(data: str):
    timestamp, bus_ids = data.splitlines()
    return int(timestamp), bus_ids


def part1(data):
    timestamp, bus_ids = data
    bus_ids = np.array([int(z) for z in bus_ids.split(",") if z != "x"])
    time_till_next_bus = bus_ids - np.mod(timestamp, bus_ids)
    return bus_ids[np.argmin(time_till_next_bus)] * np.min(time_till_next_bus)


def part2(data):
    _, bus_ids = data
    pass


if __name__ == "__main__":
    with open("input/data13.txt") as f:
        data = f.read()
    print(part1(parse(data)))


@pytest.fixture
def sample_data():
    return parse(
        """939
7,13,x,x,59,x,31,19"""
    )


def test_part_1(sample_data):
    assert part1(sample_data) == 295
