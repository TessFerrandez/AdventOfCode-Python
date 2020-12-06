CIRCUIT = {}
EVALUATED = {}


def parse_input(filename: str):
    lines = [line.strip() for line in open(filename)]

    for line in lines:
        ops, wire = line.split(' -> ')
        CIRCUIT[wire] = ops.split(' ')


def evaluate(wire: str) -> int:
    try:
        return int(wire)
    except ValueError:
        pass

    result = 0
    if wire not in EVALUATED:
        ops = CIRCUIT[wire]

        # single value
        if len(ops) == 1:
            result = evaluate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                result = evaluate(ops[0]) & evaluate(ops[2])
            if op == 'OR':
                result = evaluate(ops[0]) | evaluate(ops[2])
            if op == 'NOT':
                result = ~evaluate(ops[1]) & 0xFFFF
            if op == 'RSHIFT':
                result = evaluate(ops[0]) >> evaluate(ops[2])
            if op == 'LSHIFT':
                result = evaluate(ops[0]) << evaluate(ops[2])
        EVALUATED[wire] = result
    return EVALUATED[wire]


def part1() -> int:
    return evaluate('a')


def part2() -> int:
    a = EVALUATED['a']
    EVALUATED.clear()
    EVALUATED['b'] = a
    return evaluate('a')


def main():
    parse_input('input/day7.txt')
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    main()
