import re

with open("input/data04.txt") as f:
    data = f.read()

input_passwords = [x.split() for x in data.split("\n\n")]


input_passwords = [
    {k: v for k, v in [field.split(":") for field in passport]}
    for passport in input_passwords
]


def between(x, a, b):
    return a <= int(x) <= b


def valid_height(x):
    mode = x[-2:]
    if mode not in ["cm", "in"]:
        return False
    else:
        n = int(x[:-2])
        if mode == "cm":
            return 150 <= n <= 193
        else:
            return 59 <= n <= 76


def valid_hair_color(x):
    return x.startswith("#") and re.match(r"[\da-f]{6}", x[1:])


def valid_eye_color(x):
    return x in "amb blu brn gry grn hzl oth".split()


valid_fields = dict(
    byr=lambda yr: between(yr, 1920, 2020),  # 'Birth Year',
    iyr=lambda yr: between(yr, 2010, 2020),  # 'Issue Year',
    eyr=lambda yr: between(yr, 2020, 2030),  # 'Expiration Year',
    hgt=lambda h: valid_height(h),  # 'Height',
    hcl=lambda h: valid_hair_color(h),  # 'Hair Color',
    ecl=lambda e: valid_eye_color(e),  # 'Eye Color',
    pid=lambda n: len(n) == 9 and n.isnumeric(),  # 'Passport ID',
    cid=lambda c: True,  # 'Country ID'
)


def fields_present(passport):
    return all(passport.get(field, None) for field in valid_fields if field != "cid")


def field_data_valid(passport):
    for field in passport:
        passport_field_data = passport[field]
        if not valid_fields[field](passport_field_data):
            return False
    else:
        return True


def all_fields_passports(passports):
    return [p for p in passports if fields_present(p)]


def count_passports_valid_data(passports):
    return sum(1 for p in passports if field_data_valid(p))


def solution1(passports):
    pports = all_fields_passports(passports)
    print(len(pports))
    return pports


def solution2(passports):
    print(count_passports_valid_data(passports))


if __name__ == "__main__":
    all_fields_present_passports = solution1(input_passwords)
    solution2(all_fields_present_passports)
