from collections import defaultdict


def read_input() -> list:
    return [line.strip().split() for line in open("input/day18.txt").readlines()]


def get(value, r):
    try:
        return int(value)
    except ValueError:
        return r[value]


def puzzle1():
    send_queue = []
    instructions = read_input()
    r = defaultdict(int)
    ptr = 0

    while 0 <= ptr < len(instructions):
        instruction = instructions[ptr]
        op = instruction[0]
        p1 = instruction[1]
        p2 = None if len(instruction) == 2 else instruction[2]

        if op == "snd":
            send_queue.append(get(p1, r))
        elif op == "set":
            r[p1] = get(p2, r)
        elif op == "add":
            r[p1] += get(p2, r)
        elif op == "mul":
            r[p1] *= get(p2, r)
        elif op == "mod":
            r[p1] %= get(p2, r)
        elif op == "rcv":
            if get(p1, r) > 0:
                r[p1] = send_queue.pop()
                print("first sound:", r[p1])
                break
        elif op == "jgz":
            if get(p1, r) > 0:
                ptr += get(p2, r) - 1
        ptr += 1


def puzzle2():
    r1 = defaultdict(int)
    r2 = defaultdict(int)
    r2["p"] = 1
    regs = [r1, r2]

    ptrs = [0, 0]
    send_queue = [[], []]
    state = ["ok", "ok"]  # ok, receiving, done

    instructions = read_input()
    program = 0  # current program
    r = regs[program]
    ptr = ptrs[program]

    total_sends = 0
    while True:
        instruction = instructions[ptr]
        op = instruction[0]
        p1 = instruction[1]
        p2 = None if len(instruction) == 2 else instruction[2]

        if op == "snd":
            if program == 1:
                total_sends += 1
            send_queue[program].append(get(p1, r))
        elif op == "set":
            r[p1] = get(p2, r)
        elif op == "add":
            r[p1] += get(p2, r)
        elif op == "mul":
            r[p1] *= get(p2, r)
        elif op == "mod":
            r[p1] %= get(p2, r)
        elif op == "rcv":
            if send_queue[1 - program]:
                # other program has sent
                state[program] = "ok"
                r[p1] = send_queue[1 - program].pop(0)
            else:
                # wait and switch
                if state[1 - program] == "done":
                    break  # deadlocked
                if not send_queue[program] and state[1 - program] == "receiving":
                    break  # deadlocked
                ptrs[program] = ptr
                state[program] = "receiving"
                program = 1 - program
                ptr = ptrs[program] - 1  # will be incremented back
                r = regs[program]
        elif op == "jgz":
            if get(p1, r) > 0:
                ptr += get(p2, r) - 1

        ptr += 1
        if not 0 <= ptr < len(instructions):
            if state[1 - program] == "done":
                break  # both done
            state[program] = "done"
            ptrs[program] = ptr
            program = 1 - program
            ptr = ptrs[program]
            r = regs[program]

    print("program 1 sends:", total_sends)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
