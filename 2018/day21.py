def part1() -> int:
    d = 0

    while True:
        e = d | 0x10000
        d = 10552971
        while True:
            c = e & 0xFF
            d += c
            d &= 0xFFFFFF
            d *= 65899
            d &= 0xFFFFFF
            if 256 > e:
                return d
            # optimized
            e = e // 256


def part2() -> int:
    d = 0
    seen = set()

    while True:
        e = d | 0x10000
        d = 10552971
        while True:
            c = e & 0xFF
            d += c
            d &= 0xFFFFFF
            d *= 65899
            d &= 0xFFFFFF
            if 256 > e:
                if d not in seen:
                    print(d)
                seen.add(d)
                break
            # optimized
            e = e // 256
    return 0


def main():
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    main()
