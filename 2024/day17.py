from collections import namedtuple
from typing import Optional


def parse(data):
    lines = data.splitlines()
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = lines[4].split(': ')[1]
    return a, b, c, [int(d) for d in program.split(',')]


def run_program(a, b, c, program):
    max_ip = len(program)
    ip = 0

    def combo(operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        assert False

    out = []

    while ip < max_ip:
        op, operand = program[ip], program[ip + 1]
        if op == 0:     # adv
            a >>= combo(operand)
        elif op == 1:   # bxl
            b ^= operand
        elif op == 2:   # bst
            b = combo(operand) % 8
        elif op == 3:   # jnz
            if a != 0:
                ip = operand
                continue
        elif op == 4:   # bxc
            b ^= c
        elif op == 5:   # out
            out.append(combo(operand) % 8)
        elif op == 6:   # bdv
            b = a >> combo(operand)
        elif op == 7:
            c = a >> combo(operand)
        ip += 2

    return ','.join([str(d) for d in out])


def part1(a, b, c, program):
    return run_program(a, b, c, program)


'''
code from https://github.com/ianroberts/advent-of-code/tree/main/2024/17
'''
class BitPattern(namedtuple("BitPattern", ["mask", "pattern"])):
    def merge(self, other: "BitPattern") -> Optional["BitPattern"]:
        # to be compatible, all the bits constrained by _both_ patterns must match
        common_mask = self.mask & other.mask
        if (self.pattern & common_mask) == (other.pattern & common_mask):
            return BitPattern(self.mask | other.mask, self.pattern | other.pattern)

        # Not compatible
        return None

    def __lshift__(self, other: int):
        return BitPattern(self.mask << other, self.pattern << other)

    def __repr__(self):
        """
        Shows the masked pattern with 0 or 1 for the constrained bits and
        "." for the unconstrained ones.
        """
        mask_bin = "{:010b}".format(self.mask)
        # if the mask is more than 10 bits, zero-pad the pattern to the same length
        pat_bin = ("{:0" + str(len(mask_bin)) + "b}").format(self.pattern)
        return (
            "BitPattern("
            + "".join("." if m == "0" else p for m, p in zip(mask_bin, pat_bin))
            + ")"
        )


def generate_base_patterns(k1, k2):
    # k1 and k2 are magic constants from the input program
    patterns = []
    for n in range(8):
        n_patterns = set()
        for b in range(8):
            # constraint on the lowest three bits
            b_pattern = BitPattern(7, b ^ k1 ^ k2)
            # constraint on some set of three other bits somewhere between
            # positions 0 and 10
            c_pattern = BitPattern(7, n ^ b) << (b ^ k2)
            merged = b_pattern.merge(c_pattern)
            if merged:
                n_patterns.add(merged)
        patterns.append(n_patterns)

    return patterns


def part2(program, k1, k2):
    base_patterns = generate_base_patterns(k1, k2)
    # Debug base patterns
    print("Base patterns:")
    for n, pats in enumerate(base_patterns):
        print(n)
        print(*pats, sep="\n")

    candidates = set(base_patterns[program[0]])
    for i in range(1, len(program)):
        target_value = program[i]
        new_candidates = set()
        # Patterns for this digit will constrain bits starting at position 3i
        # (counting from the right)
        this_number_patterns = set(p << (3 * i) for p in base_patterns[target_value])
        # attempt to merge each of the new patterns for this digit with each of the
        # existing patterns for the sequence so far, discarding any that conflict.
        for tail_pattern in candidates:
            for pattern in this_number_patterns:
                merged = tail_pattern.merge(pattern)
                if merged:
                    new_candidates.add(merged)

        if not new_candidates:
            raise ValueError("This program cannot generate itself")

        candidates = new_candidates
        print(f"{len(candidates)} candidates remain after iteration {i}")

    # we now have all the patterns that could match an initial "a" register,
    # the smallest number that could match any of these patterns happens to be
    # exactly the decimal value of the smallest pattern, since we've been
    # careful to ensure that all non-constrained bits in every pattern are
    # left as zero at all steps
    return min(p.pattern for p in candidates)


def test():
    data = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
    a, b, c, program = parse(data)
    assert part1(a, b, c, program) == '4,6,3,5,6,3,5,2,1,0'


test()
data = '''Register A: 63281501
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0'''
a, b, c, program = parse(data)
k1, k2 = 5, 6
print('Part1:', part1(a, b, c, program))
print('Part2:', part2(program, k1, k2))
