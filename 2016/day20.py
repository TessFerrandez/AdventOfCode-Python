def read_input() -> list:
    lines = [
        [int(part) for part in line.strip().split("-")]
        for line in open("input/day20.txt").readlines()
    ]
    lines.sort()
    return lines


def count_available(ip_ranges: list) -> int:
    blocked = 0
    for ip_range in ip_ranges:
        blocked += ip_range[1] - ip_range[0] + 1
    return 4294967296 - blocked


def make_clusters(ip_ranges: list) -> list:
    current = ip_ranges[0]
    ranges = []
    for ip_range in ip_ranges:
        if ip_range[0] <= current[1] + 1:
            current[1] = max(current[1], ip_range[1])
        else:
            ranges.append(current.copy())
            current = ip_range
    ranges.append(current)
    return ranges


def puzzles():
    ip_ranges = read_input()
    ranges = make_clusters(ip_ranges)
    print("first available:", ranges[0][1] + 1)
    print(count_available(ranges), "available ips")


if __name__ == "__main__":
    puzzles()
