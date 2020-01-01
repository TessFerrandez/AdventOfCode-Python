def knot_hash(data):
    data = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    nums = [i for i in range(256)]
    i = 0
    skip_size = 0
    for _ in range(64):
        for d in data:
            for j in range(d // 2):
                nums[(i + j) % len(nums)], nums[(i + (d - j - 1)) % len(nums)] = (
                    nums[(i + (d - j - 1)) % len(nums)],
                    nums[(i + j) % len(nums)],
                )
            i += d + skip_size
            i = i % len(nums)
            skip_size += 1

    dense_hash = []
    for i in range(16):
        x = 0
        for j in range(16):
            x = x ^ nums[i * 16 + j]
        dense_hash.append(x)

    s = ""
    for c in dense_hash:
        s += "{0:02x}".format(c)
    return s
