import math

with open('input/data03.txt') as f:
    data = [x.rstrip() for x in f.readlines()]


def count_trees(data, dx, dy):
    trees = 0
    x, y = 0, 0
    while y < len(data):
        if data[y][x] == '#':
            trees += 1
        y += dy
        x = (x + dx) % len(data[0])
    return trees


# part 1
print(count_trees(data, 3, 1))
# part 2
answer = math.prod(count_trees(data, dx, dy)
                   for dx, dy in zip([1, 3, 5, 7, 1], [1]*4+[2]))
print(answer)
