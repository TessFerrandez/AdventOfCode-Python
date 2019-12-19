import re


def get_islands(input_list: list) -> list:
    prev_island_len = 0

    while True:
        final_groups = []

        for group in input_list:
            did_intersect = False
            for f_group in final_groups:
                if len(f_group.intersection(group)) > 0:
                    f_group |= set(group)
                    did_intersect = True
            if not did_intersect:
                final_groups.append(set(group))

        new_len = len(final_groups)
        if new_len != prev_island_len:
            input_list = final_groups.copy()
            prev_island_len = new_len
            continue

        return final_groups


def puzzles():
    programs_groups = [[int(number) for number in re.findall(r'[\d]+', line)] for line in open("input/day12.txt").readlines()]
    islands = get_islands(programs_groups)
    for island in islands:
        if 0 in island:
            print("Island length: ", len(island))
            break
    print("total islands:", len(islands))


if __name__ == "__main__":
    puzzles()
