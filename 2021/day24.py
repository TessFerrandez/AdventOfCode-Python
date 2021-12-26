"""
Translated and optimized version of the ALU code

The result is 0 if
    W[0] == W[11] - 4
    W[1] == W[10] + 5
    W[2] == W[9] - 3
    W[3] == W[4] + 7
    W[5] == W[6]
    W[7] == W[8] - 5
    W[12] == W[13] + 1
"""


def get_z(W):
    z = W[0] + 12
    z = (26 * z) + W[1] + 8
    z = (26 * z) + W[2] + 7

    if W[3] != W[4] + 7:
        z = (z * 26) + W[4] + 4

    if W[5] != W[6]:
        z = (z * 26) + W[6] + 10

    if W[7] != W[8] - 5:
        z = (z * 26) + W[8] + 12

    # if all the ifs above are false
    # the number is as low as possible
    # and x is W[2] + 7 - 4 = W[2] + 3
    # so to minimize W[9] == W[2] + 3
    x = (z % 26) - 4
    z //= 26

    if x != W[9]:
        z = (z * 26) + W[9] + 10

    # if all the ifs above are false
    # the number is as low as possible
    # and x is W[1] + 8 - 13 = W[1] - 5
    # so to minimize W[10] + 5 == W[1]
    x = (z % 26) - 13
    z //= 26

    if x != W[10]:
        z = (z * 26) + W[10] + 15

    # if all the ifs above are false
    # the number is as low as possible
    # and x is W[0] + 12 - 8 = W[0] + 4
    # so to minimize W[0] + 4 == W[11]
    x = (z % 26) - 8
    z //= 26

    if x != W[11]:
        z = (z * 26) + W[11] + 4

    if W[12] != W[13] + 1:
        z = (z * 26) + W[13] + 9

    return z


def get_result(number) -> int:
    inputs = [int(n) for n in str(number)]
    return get_z(inputs)


maximum = 59692994994998
print("Part 1:", maximum, get_result(maximum))

minimum = 16181111641521
print("Part 2:", minimum, get_result(minimum))
