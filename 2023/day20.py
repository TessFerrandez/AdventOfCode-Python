from collections import deque
from input_processing import read_data
from math import gcd


class Gate:
    def __init__(self, description):
        self.inputs = {}
        self.outputs = []
        self.on = False
        self.type = 'simple'

        if ' -> ' not in description:
            self.name = description
        else:
            name, description = description.split(' -> ')
            if name.startswith('&'):
                self.type = 'conjunction'
                self.name = name[1:]
            elif name.startswith('%'):
                self.type = 'flip-flop'
                self.name = name[1:]
            else:
                self.type = 'simple'
                self.name = name
            self.outputs = description.split(', ')

    def __repr__(self):
        if self.type == 'simple':
            return f'{self.name}:{self.type} -> out:{self.outputs}'
        elif self.type == 'conjunction':
            return f'{self.name}:{self.type} -> in:{self.inputs} -> out:{self.outputs}'
        else:
            return f'{self.name}:{self.type}:{"on" if self.on else "off"} -> out:{self.outputs}'


def parse(data):
    gates = {}

    for line in data.splitlines():
        gate = Gate(line)
        gates[gate.name] = gate

    to_add = set()
    for gate_name in gates:
        gate = gates[gate_name]
        for output in gate.outputs:
            if output not in gates:
                to_add.add((output, gate_name))
            else:
                gates[output].inputs[gate_name] = False

    for gate_to_add, gate_input in to_add:
        if gate_to_add not in gates:
            gates[gate_to_add] = Gate(gate_to_add)
        gates[gate_to_add].inputs[gate_input] = False

    return gates


def push_button(gates, count=False):
    queue = deque([('button', 'broadcaster', False)])
    high_count = 0
    low_count = 0

    mk = fp = xt = zc = False

    while queue:
        from_gate, to_gate, is_high = queue.popleft()
        if count and to_gate == 'rx':
            if gates['kl'].inputs['mk']:
                mk = True
            if gates['kl'].inputs['fp']:
                fp = True
            if gates['kl'].inputs['xt']:
                xt = True
            if gates['kl'].inputs['zc']:
                zc = True

        if is_high:
            high_count += 1
        else:
            low_count += 1

        gate = gates[to_gate]
        if gate.type == 'simple':
            for output in gate.outputs:
                queue.append((to_gate, output, is_high))
        elif gate.type == 'flip-flop':
            if not is_high:
                gate.on = not gate.on
                for output in gate.outputs:
                    queue.append((to_gate, output, gate.on))
        else:
            gate.inputs[from_gate] = is_high
            if all(gate.inputs.values()):
                for output in gate.outputs:
                    queue.append((to_gate, output, False))
            else:
                for output in gate.outputs:
                    queue.append((to_gate, output, True))

    if count:
        return gates, high_count, low_count, mk, fp, xt, zc

    return gates, high_count, low_count


def all_low(gates):
    for gate in gates.values():
        if gate.type == 'flip-flop' and gate.on:
            return False
    return True


def part1(gates):
    total_high = total_low = 0

    for _ in range(1000):
        gates, high_count, low_count = push_button(gates)
        total_high += high_count
        total_low += low_count

    return total_high * total_low


def part2(gates):
    total_high = total_low = 0

    cycles = {}

    i = 0
    for i in range(1, 10000):
        gates, high_count, low_count, mk, fp, xt, zc = push_button(gates, count=True)
        if mk and "mk" not in cycles:
            cycles["mk"] = i
        if fp and "fp" not in cycles:
            cycles["fp"] = i
        if xt and "xt" not in cycles:
            cycles["xt"] = i
        if zc and "zc" not in cycles:
            cycles["zc"] = i
        total_high += high_count
        total_low += low_count

    lcm = 1
    for cycle in cycles.values():
        lcm = lcm * cycle // gcd(lcm, cycle)

    return lcm


def test():
    sample = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''
    gates = parse(sample)
    assert part1(gates) == 32000000
    sample2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''
    gates = parse(sample2)
    assert part1(gates) == 11687500


test()
data = read_data(2023, 20)
gates = parse(data)
print('Part1:', part1(gates))
gates = parse(data)
print('Part2:', part2(gates))
