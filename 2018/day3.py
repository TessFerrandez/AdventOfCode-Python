import re


def puzzle1():
    w, h = 1000, 1000
    sheet = [[0 for x in range(w)] for y in range(h)]

    with open('input/day3.txt') as f:
        for line in f:
            data = line.split(' ')
            pos = [int(element) for element in data[2][:-1].split(',')]
            area = [int(element) for element in data[3].split('x')]

            for x in range(pos[0], pos[0] + area[0]):
                for y in range(pos[1], pos[1] + area[1]):
                    sheet[x][y] += 1

    count = 0
    for x in range(0, w):
        for y in range(0, h):
            if sheet[x][y] > 1:
                count += 1

    print("inches of fabric in 2 or more claims:", count)


def puzzle2():
    width, height = 1000, 1000
    sheet = [[0 for x in range(width)] for y in range(height)]

    claims = [re.split(r'[@,:x]', line)
              for line in open('input/day3.txt').readlines()]
    claims = [[claim[0].strip(),
               int(claim[1]), int(claim[2]), int(claim[3]), int(claim[4])]
              for claim in claims]

    for claim in claims:
        for x in range(claim[1], claim[1] + claim[3]):
            for y in range(claim[2], claim[2] + claim[4]):
                sheet[x][y] += 1

    for claim in claims:
        overlaps = False
        for x in range(claim[1], claim[1] + claim[3]):
            for y in range(claim[2], claim[2] + claim[4]):
                if sheet[x][y] > 1:
                    overlaps = True

        if not overlaps:
            print("ID of non-overlapping claim:", claim[0])
            break


if __name__ == "__main__":
    puzzle1()
    puzzle2()
