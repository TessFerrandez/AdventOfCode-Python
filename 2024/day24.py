from dataclasses import dataclass
from input_processing import read_data
import re
import logging


logger = logging.getLogger(__name__)


def parse(data):
    wire_data, gates_data = data.split('\n\n')
    wires = {}
    for wire in wire_data.splitlines():
        name, value = wire.split(': ')
        wires[name] = int(value)
    gates = {}
    for gate in gates_data.splitlines():
        action, result = gate.split(' -> ')
        wire_a, op, wire_b = action.split(' ')
        gates[result] = (wire_a, op, wire_b)
    return wires, gates


@dataclass
class Operation():
    left_wire: str
    right_wire: str
    gate: str
    output_wire: str

    def __str__(self):
        return f'{self.output_wire} = {self.left_wire} {self.gate} {self.right_wire}'


def parse2(data):
    gate_regex = re.compile(r"(\w+) (XOR|OR|AND) (\w+) -> (\w+)")
    wires: dict[str, int] = dict()
    operations: dict[str, tuple] = {}

    wires_lines, connections_lines = [block.splitlines() for block in data.split('\n\n')]
    wires = {wire: int(value) for wire, value in (line.split(': ') for line in wires_lines)}
    logger.debug(wires)
    logger.debug(connections_lines)

    for line in connections_lines:
        match = gate_regex.match(line)
        if not match:
            raise ValueError(f"Invalid line: {line}")
        left_wire, gate, right_wire, output_wire = match.groups()
        operations[output_wire] = Operation(left_wire, right_wire, gate, output_wire)

    return wires, operations


def part1(wires, gates):
    def evaluate(wire):
        if wire in wires:
            return wires[wire]
        wire_a, op, wire_b = gates[wire]
        wire_a = evaluate(wire_a)
        wire_b = evaluate(wire_b)
        if op == 'AND':
            wires[wire] = wire_a & wire_b
        elif op == 'OR':
            wires[wire] = wire_a | wire_b
        elif op == 'XOR':
            wires[wire] = wire_a ^ wire_b
        return wires[wire]

    result_wires = [wire for wire in gates if wire[0] == 'z']
    results = [0 for _ in range(len(result_wires))]
    for wire in result_wires:
        results[int(wire[1:])] = evaluate(wire)
    results = results[::-1]
    return int(''.join(str(bit) for bit in results), 2)


def execute_gate(gate, left_wire, right_wire):
    match gate:
        case "AND":
            return left_wire & right_wire
        case "OR":
            return left_wire | right_wire
        case "XOR":
            return left_wire ^ right_wire
        case _:
            raise ValueError(f"Invalid gate: {gate}")


def process_output(output, wires, operations, depth = 0, max_depth = 100):
    if depth > max_depth:
        raise RecursionError("Max depth reached")
    if output in wires:
        return wires[output]
    result = execute_gate(
        operations[output].gate,
        process_output(operations[output].left_wire, wires, operations, depth + 1),
        process_output(operations[output].right_wire, wires, operations, depth + 1))
    wires[output] = result
    return wires[output]


def get_output_for_wire_type(wires, wire_type):
    sorted_wires = sorted(((wire, value) for wire,value in wires.items() if wire.startswith(wire_type)),
                          key=lambda x: x[0],
                          reverse=True) # E.g. [('z05', 0), ('z04', 1), ...]

    output_as_bin_str = ("".join(str(value) for _, value in sorted_wires)) # E.g. '0110101'
    output_as_dec = int(output_as_bin_str, 2) # E.g. 53
    return output_as_dec


def part1_2(wires, operations):
    local_wires = wires.copy()
    for output in operations.keys():
        if output.startswith("z"):
            process_output(output, local_wires, operations)
    z_out = get_output_for_wire_type(local_wires, "z")
    print(z_out)


def part2(wires, operations):
    pass


def test():
    data = '''x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj'''
    wires, gates = parse(data)
    assert part1(wires, gates) == 2024


test()
data = read_data(2024, 24)
wires, gates = parse(data)
print('Part1:', part1(wires, gates))
wires, gates = parse2(data)
print('Part2:', part2(wires, gates))
