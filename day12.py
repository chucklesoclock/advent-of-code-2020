import pytest
import math


def parse(data: str):
    return [(instruction[0], int(instruction[1:])) for instruction in data.splitlines()]


def part1(data):
    direction = 0
    position = [0, 0]
    for action, num in data:
        match action:
            case "N":
                position[1] += num
            case "S":
                position[1] -= num
            case "E":
                position[0] += num
            case "W":
                position[0] -= num
            case "R":
                direction -= num
                direction = direction % 360
            case "L":
                direction += num
                direction = direction % 360
            case "F":
                position[0] += int(math.cos(math.radians(direction)) * num)
                position[1] += int(math.sin(math.radians(direction)) * num)
    return sum(abs(d) for d in position)


def part2(data):
    waypoint = [10, 1]
    position = [0, 0]
    for action, num in data:
        match (action, num):
            case ("N", _):
                waypoint[1] += num
            case ("S", _):
                waypoint[1] -= num
            case ("E", _):
                waypoint[0] += num
            case ("W", _):
                waypoint[0] -= num
            case ("R", 90) | ("L", 270):
                # rotate waypoint around ship clockwise
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            case ("R", 180) | ("L", 180):
                # flip waypoint to other side
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            case ("R", 270) | ("L", 90):
                # rotate waypoint around ship counterclockwise
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            case ("F", _):
                position[0] += waypoint[0] * num
                position[1] += waypoint[1] * num

    return sum(abs(d) for d in position)


if __name__ == "__main__":
    with open("input/data12.txt") as f:
        data = parse(f.read())
    print(part1(data))
    print(part2(data))


@pytest.fixture
def sample_data():
    return parse(
        """F10
N3
F7
R90
F11"""
    )


def test_part_1(sample_data):
    assert part1(sample_data) == 25


def test_part_2(sample_data):
    assert part2(sample_data) == 286
