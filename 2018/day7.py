def read_input() -> (dict, list):
    chains = dict()
    lines = [line.strip().split(" ") for line in open("input/day7.txt").readlines()]
    for line in lines:
        before, after = line[1], line[7]
        if after in chains:
            chains[after].append(before)
        else:
            chains[after] = [before]

    steps = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # steps = [c for c in "ABCDEF"]

    # any steps with no pre-reqs
    # are executable
    available_steps = []
    for i in range(len(steps)):
        if steps[i] not in chains:
            available_steps.append(steps[i])

    return chains, available_steps


def update_chains(chains: dict, step: str) -> list:
    available_steps = []

    # any steps without pre-reqs
    # are now executable
    for chain in chains:
        if step in chains[chain]:
            chains[chain].remove(step)
            if not chains[chain]:
                if step not in available_steps:
                    available_steps.append(chain)
    return available_steps


def puzzle1():
    chains, available_steps = read_input()
    order = ""

    while available_steps:
        # execute next available step
        available_steps.sort()
        step = available_steps[0]
        available_steps.pop(0)
        order += step

        available_steps += update_chains(chains, step)

    print("order:", order)


def workers_done(workers: list) -> bool:
    for worker in workers:
        if worker[0] != 0:
            return False
        if worker[1] != ".":
            return False
    return True


def puzzle2(num_workers: int, delay: int):
    chains, available_steps = read_input()

    # set up available workers
    workers = []
    for _ in range(num_workers):
        workers.append([0, "."])

    seconds = 0
    while available_steps or not workers_done(workers):
        seconds += 1
        print(available_steps, workers)
        for i in range(num_workers):
            if workers[i][0] == 0:
                # if we finished a step - release it
                if workers[i][1] != ".":
                    available_steps += update_chains(chains, workers[i][1])

        for i in range(num_workers):
            if workers[i][0] == 0:
                # take on a new step
                if available_steps:
                    step = available_steps[0]
                    workers[i][0] = ord(step) - 65 + delay
                    workers[i][1] = step
                    available_steps.pop(0)
                else:
                    workers[i][1] = "."
            else:
                workers[i][0] -= 1
    seconds -= 1
    print("seconds:", seconds)


if __name__ == "__main__":
    puzzle1()
    puzzle2(5, 60)
