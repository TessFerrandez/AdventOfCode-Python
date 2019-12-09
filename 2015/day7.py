import re
calc = dict()
results = dict()


def calculate(wire):
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in results:
        ops = calc[wire]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
                res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
                res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
                res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
                res = calculate(ops[0]) << calculate(ops[2])
        results[wire] = res
    return results[wire]


def init_wiring(commands):
    for command in commands:
        (ops, res) = command.split('->')
        calc[res.strip()] = ops.strip().split(' ')


def puzzle1():
    init_wiring(open('input/day7.txt'))
    print("result for a: ", calculate('a'))
    results.clear()
    results['b'] = 46065
    print("result for a: ", calculate('a'))


if __name__ == "__main__":
    puzzle1()
