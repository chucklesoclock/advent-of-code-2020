import numpy as np

with open('input/data06.txt') as f:
    data = f.read().split('\n\n')


def group_yes_counts(group):
    group = group.split('\n')
    any_yes = set(group[0])
    all_yes = any_yes.copy()
    for person in group[1:]:
        answer_set = set(person)
        any_yes.update(answer_set)
        all_yes.intersection_update(answer_set)
    return len(any_yes), len(all_yes)


if __name__ == "__main__":
    any_yes_sum, all_yes_sum = np.sum(
        [group_yes_counts(group) for group in data], axis=0)
    print('any =', any_yes_sum)
    print('all =', all_yes_sum)
