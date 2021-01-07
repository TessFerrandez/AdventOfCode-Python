from typing import List
from Computer import Computer, InputInterrupt, OutputInterrupt


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def get_image(code: List[int]) -> str:
    computer = Computer(code)
    image = ''
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            print('need input')
            break
        except OutputInterrupt:
            ch = computer.outputs[-1]
            image += chr(ch)
    return image


def part1(code: List[int]) -> int:
    image = get_image(code)
    # print(image)

    grid = [line for line in image.strip().split(chr(10))]
    height, width = len(grid), len(grid[0])

    intersections = []
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] == '#' and grid[y - 1][x] == '#' and grid[y + 1][x] == '#' and grid[y][x - 1] == '#' and grid[y][x + 1] == '#':
                intersections.append((x, y))

    return sum(x * y for x, y in intersections)


def part2(code: List[int]) -> int:
    code[0] = 2
    computer = Computer(code)
    dust = 0

    main_routine = 'A,B,A,B,C,C,B,A,B,C\n'
    a_routine = 'L,8,R,12,R,12,R,10\n'
    b_routine = 'R,10,R,12,R,10\n'
    c_routine = 'L,10,R,10,L,6\n'
    complete_routine = main_routine + a_routine + b_routine + c_routine + 'n\n'

    ascii_routine = [ord(ch) for ch in complete_routine]
    i = 0
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            computer.inputs.append(ascii_routine[i])
            i += 1
        except OutputInterrupt:
            result = computer.outputs[-1]
            if result > 1000:
                return result
            print(chr(result), end='')
    return dust


def main():
    code = parse_input('input/day17.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day17.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
