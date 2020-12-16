import itertools

with open("input/data09.txt") as f:
    data = [int(x) for x in f.readlines()]

preamble = 25

for i in range(preamble, len(data)):
    window = data[i - preamble : i]
    n = data[i]
    # recalculating all the sums is inefficient
    # i should only have to drop and add n=preamble-1 sums
    if n not in (sum(tup) for tup in itertools.combinations(window, 2)):
        invalid = n
        print(n)
        break
else:
    raise Exception("all numbers are sum of 2 numbers in preamble")

d = [(i, x) for i, x in enumerate(data) if x < invalid]
# this errors
sub_sequences = []
for i in reversed(range(1, len(d))):
    data_idx = d[i][0]
    previous_data_idx = d[i - 1][0]
    out_of_sequence_with_previous = data_idx - 1 != previous_data_idx
    if i == len(d) - 1 and out_of_sequence_with_previous:
        print(f"idx = {data_idx: >3} deleted")
        del d[i]
    else:
        out_of_sequence_with_next = data_idx + 1 != d[i + 1][0]
        if out_of_sequence_with_previous:
            if out_of_sequence_with_next:
                print(f"idx = {data_idx: >3} deleted")
                del [i]
            else:
                sub_sequences.append(d[-i:])
                print(f"append d[{-i}:{len(d)-1}]")
                del d[i:]
else:
    sub_sequences.append(d[0:])
    del d[0:]

