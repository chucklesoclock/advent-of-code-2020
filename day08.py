with open('input/data08.txt') as f:
    code = f.read().splitlines()


def part1():
    visited = [False] * len(code)

    i = 0
    accumulator = 0

    while not visited[i]:
        visited[i] = True
        cmd, n = code[i].split()
        if cmd == 'acc':
            accumulator += int(n)
            i += 1
        elif cmd == 'jmp':
            i += int(n)
        else:
            i += 1
    else:
        print(f'acc before infinite loop = {accumulator}'.rjust(40))


def part2():

    def check_code(code):
        visited = [False] * len(code)

        i = 0
        accumulator = 0

        while not visited[i]:
            visited[i] = True
            cmd, n = code[i].split()
            if cmd == 'acc':
                accumulator += int(n)
                i += 1
            elif cmd == 'jmp':
                i += int(n)
            else:
                i += 1
            if i >= len(code):
                return accumulator
        else:
            return None

    for idx, line in enumerate(code):
        cmd, _ = line.split()
        if not cmd == 'acc':
            # pass code with line swapped
            line_swapped_code = code[:idx] + [code[idx].replace(
                cmd, 'jmp' if cmd == 'nop' else 'nop', 1)] + code[idx+1:]
            accumulator = check_code(line_swapped_code)
            # return accumulator if code doesn't loop
            if accumulator is not None:
                print(
                    f'acc on successful termination = {accumulator}'.rjust(40))
                break
    else:
        print('Error: switching all eligible lines does not fix program')


if __name__ == "__main__":
    part1()
    part2()
