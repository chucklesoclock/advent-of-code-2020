with open('input/data06.txt') as f:
    data = f.read().split('\n\n')


def group_yes_count(group):
    yes_answers = set()
    for person in group.split('\n'):
        yes_answers.update({ch for ch in person})
    return len(yes_answers)


def part1():
    return sum(group_yes_count(group) for group in data)


if __name__ == "__main__":
    print(part1())
