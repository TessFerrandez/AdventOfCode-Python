from typing import List


def part1(fish: List[int]) -> int:

    for day in range(80):
        born = 0
        for i, nemo in enumerate(fish):
            if nemo == 0:
                fish[i] = 6
                born += 1
            else:
                fish[i] -= 1

        print(day, born)
        for baby in range(born):
            fish.append(8)

        if day == 17:
            print(len(fish))

    return len(fish)


print(part1([3, 4, 3, 1, 2]))
