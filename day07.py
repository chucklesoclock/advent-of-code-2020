with open('input/data07.txt') as f:
    data = f.read().splitlines()
# 'shiny cyan bags contain 4 plaid green bags, 4 dim coral bags, 4 dull indigo bags.'


def part1():
    d = dict()
    for line in data:
        k, v = line.split(' contain ')
        k = k[:-len(' bags')]
        v = [''.join(ch for ch in x.replace('bags', 'bag').replace(
            ' bag', '') if not ch.isnumeric()).strip() for x in v.rstrip('.').split(', ')]
        d[k] = v if not v[0] == 'no other' else []

    def can_carry_shiny(bag):
        sub_bags = d[bag]
        if not sub_bags:
            return False
        else:
            return 'shiny gold' in sub_bags or any(can_carry_shiny(b) for b in sub_bags)

    print(sum(can_carry_shiny(bag) for bag in d))


def part2():
    d = dict()
    for line in data:
        k, v = line.split(' contain ')
        k = k[:-len(' bags')]
        v = [x.replace('bags', 'bag').replace(' bag', '')
             for x in v.rstrip('.').split(', ')]
        if v[0] == 'no other':
            vd = dict()
        else:
            vd = dict()
            for bag in v:
                n, bag = bag.split(' ', 1)
                vd[bag] = int(n)
        d[k] = vd

    def count_bags(bag):
        sub_bags = d[bag]
        if not sub_bags:
            return 0
        else:
            return sum(sub_bags[b] * (1 + count_bags(b)) for b in sub_bags)

    print(count_bags('shiny gold'))


if __name__ == "__main__":
    part1()
    part2()
