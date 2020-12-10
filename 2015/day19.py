import pytest
import re
from collections import defaultdict
from typing import List


@pytest.mark.parametrize('replacements, molecule, expected',
                         [
                             ([['H', 'HO'], ['H', 'OH'], ['O', 'HH']], 'HOH', 4),
                         ])
def test_part1(replacements: List[List[str]], molecule: str, expected: int):
    assert part1(replacements, molecule) == expected


@pytest.mark.parametrize('replacements, molecule, expected',
                         [
                             ([['e', 'H'], ['e', 'O'], ['H', 'HO'], ['H', 'OH'], ['O', 'HH']], 'HOH', 3),
                         ])
def test_part2(replacements: List[List[str]], molecule: str, expected: int):
    assert part2(replacements, molecule) == expected


def parse_input(filename: str) -> (dict, str):
    *lines, _, molecule = open(filename).readlines()
    replacements = [line.strip().split(' => ') for line in lines]
    return replacements, molecule


def part1(replacements: List[List[str]], molecule: str) -> int:
    generated = set()
    for before, after in replacements:
        for i in range(len(molecule)):
            if molecule[i: i + len(before)] == before:
                generated.add(molecule[: i] + after + molecule[i + len(before):])
    return len(generated)


def part2(replacements: List[List[str]], molecule: str) -> int:
    original_replacements = replacements.copy()

    steps = 0
    current_molecule = molecule

    while current_molecule != 'e':
        try:
            replacement = max(replacements, key=lambda x: len(x[1]))
        except ValueError:
            replacements = original_replacements.copy()
            replacement = max(replacements, key=lambda x: len(x[1]))
        before, after = replacement
        new_molecule = current_molecule.replace(after, before, 1)
        if current_molecule != new_molecule:
            steps += 1
        else:
            replacements.remove(replacement)
        current_molecule = new_molecule
    return steps


def main():
    replacements, molecule = parse_input('input/day19.txt')
    print(f'Part 1: {part1(replacements, molecule)}')
    print(f'Part 2: {part2(replacements, molecule)}')


if __name__ == "__main__":
    main()
