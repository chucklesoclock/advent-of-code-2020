with open("input/data05.txt") as f:
    data = f.readlines()


def binary_search(code, lower_lim, upper_lim):
    dist = upper_lim - lower_lim + 1
    if dist == 1:
        assert lower_lim == upper_lim
        return upper_lim
    else:
        try:
            if code[0] in "FL":
                upper_lim -= dist // 2
            elif code[0] in "BR":
                lower_lim += dist // 2
        except IndexError as e:
            print(f"Ran out of code string without returning: {e}")
            print(f"  > [lower, upper] = [{lower_lim}, {upper_lim}]")
            raise
        else:
            return binary_search(code[1:], lower_lim, upper_lim)


ids = []
max_id = 0
for bpass in data:
    row_code, col_code = bpass[:7], bpass[7:]
    row = binary_search(row_code, 0, 127)
    col = binary_search(col_code, 0, 7)
    seat_id = row * 8 + col
    ids.append(seat_id)
    # print(f'row = {row: >3}, col = {col: >2}, seat ID = {seat_id}')
    if seat_id > max_id:
        max_id = seat_id
print(f">>>> max seat ID = {max_id}")
my_seat = set(range(min(ids), max(ids) + 1)).difference(set(ids))
print(f">>>> my seat ID  = {my_seat.pop()}")
