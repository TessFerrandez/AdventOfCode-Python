from typing import NamedTuple, List
from dataclasses import dataclass
import enum
import itertools
import collections


class Point(NamedTuple('Point', [('x', int), ('y', int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def nb4(self):
        return [self + d for d in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]]


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


@dataclass
class Unit:
    team: Team
    position: Point
    hp: int = 200
    alive: bool = True
    power: int = 3


class ElfDied(Exception):
    pass


class Arena(dict):
    def __init__(self, lines, power=3):
        super().__init__()

        self.units = []

        for y, line in enumerate(lines):
            for x, el in enumerate(line):
                self[Point(y, x)] = el == '#'

                if el in 'EG':
                    self.units.append(Unit(
                        team={'E': Team.ELF, 'G': Team.GOBLIN}[el],
                        position=Point(y, x),
                        power={'E': power, 'G': 3}[el]
                    ))

    def play(self, elf_death=False) -> int:
        rounds = 0
        while True:
            if self.round(elf_death=elf_death):
                break
            rounds += 1
        return rounds * sum(unit.hp for unit in self.units if unit.alive)

    def round(self, elf_death=False) -> bool:
        for unit in sorted(self.units, key=lambda u: u.position):
            if unit.alive:
                if self.move(unit, elf_death=elf_death):
                    return True

    def move(self, unit, elf_death=False) -> bool:
        targets = [target for target in self.units if unit.team != target.team and target.alive]
        occupied = set(u2.position for u2 in self.units if u2.alive and unit != u2)

        if not targets:
            return True

        in_range = set(pt for target in targets for pt in target.position.nb4 if not self[pt] and pt not in occupied)

        if unit.position not in in_range:
            move = self.find_move(unit.position, in_range)

            if move:
                unit.position = move

        opponents = [target for target in targets if target.position in unit.position.nb4]

        if opponents:
            target = min(opponents, key=lambda u: (u.hp, u.position))

            target.hp -= unit.power

            if target.hp <= 0:
                target.alive = False
                if elf_death and target.team == Team.ELF:
                    raise ElfDied()

    def find_move(self, position, targets) -> int:
        visiting = collections.deque([(position, 0)])
        meta = {position: (0, None)}
        seen = set()
        occupied = {unit.position for unit in self.units if unit.alive}

        while visiting:
            pos, dist = visiting.popleft()
            for nb in pos.nb4:
                if self[nb] or nb in occupied:
                    continue
                if nb not in meta or meta[nb] > (dist + 1, pos):
                    meta[nb] = (dist + 1, pos)
                if nb in seen:
                    continue
                if not any(nb == visit[0] for visit in visiting):
                    visiting.append((nb, dist + 1))
            seen.add(pos)

        try:
            min_dist, closest = min((dist, pos) for pos, (dist, parent) in meta.items() if pos in targets)
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest


def parse_input(filename: str) -> List[str]:
    return open(filename).read().splitlines()


def part1(lines: List[str]) -> int:
    arena = Arena(lines)
    return arena.play()


def part2(lines: List[str]) -> int:
    for power in itertools.count(4):
        try:
            outcome = Arena(lines, power).play(elf_death=True)
        except ElfDied:
            continue
        else:
            return outcome
    return 0


def main():
    lines = parse_input('input/day15_test.txt')
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')


if __name__ == "__main__":
    main()
