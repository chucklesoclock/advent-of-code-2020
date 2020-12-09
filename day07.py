with open('input/data07.txt') as f:
    data = f.read().splitlines()

d = dict()
for line in data:
    k, v = line.split(' contain ')
    k = k[:-len(' bags')]
    v = [''.join(ch for ch in x.replace('bags', 'bag').replace(
        ' bag', '') if not ch.isnumeric()).strip() for x in v.rstrip('.').split(', ')]
    d.update({k: v if not v[0] == 'no other' else []})


def can_carry_shiny(bag):
    sub_bags = d[bag]
    if not sub_bags:
        return False
    else:
        return 'shiny gold' in sub_bags or any(can_carry_shiny(b) for b in sub_bags)


print(sum(can_carry_shiny(bag) for bag in d))
