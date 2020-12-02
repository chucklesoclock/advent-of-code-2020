with open('data.txt') as f:
    data = list({int(x.strip()) for x in f.readlines()})


def find_solution1(data, total):
    for i, x in enumerate(data[:-1]):
        for y in data[i+1:]:
            if x + y == total:
                return x * y
    else:
        return None


def find_solution2(data):
    for i, n in enumerate(data[:-2]):
        add_result = find_solution1(data[i+1:], 2020-n)
        if add_result:
            return n * add_result
    else:
        return None


print(find_solution1(data, 2020))
print(find_solution2(data))
