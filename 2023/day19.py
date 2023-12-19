from collections import deque
from input_processing import read_data
import math


def parse(data):
    workflow_data, parts_data = data.split('\n\n')

    workflows = {}

    for line in workflow_data.splitlines():
        name, rules_data = line.split('{')
        rules = []

        for rule in rules_data[:-1].split(','):
            rule_parts = rule.split(':')
            if len(rule_parts) == 2:
                rating_type, condition, value = rule_parts[0][0], rule_parts[0][1], rule_parts[0][2:]
                result = rule_parts[1]
                rules.append((rating_type, condition, int(value), result))
            else:
                rules.append(rule_parts[0])

        workflows[name] = rules

    parts = []
    for part_data in parts_data.splitlines():
        part_bits = part_data[1:-1].split(',')
        parts.append({part_bits[0]: int(part_bits[2:]) for part_bits in part_bits})

    return workflows, parts


def apply_workflow(workflow, workflows, part):
    workflow_result = None
    for rule in workflows[workflow][:-1]:
        rating_type, condition, value, if_true = rule
        if condition == '<':
            if part[rating_type] < value:
                workflow_result = if_true
        elif condition == '>':
            if part[rating_type] > value:
                workflow_result = if_true
        if workflow_result:
            break
    if not workflow_result:
        workflow_result = workflows[workflow][-1]

    if workflow_result in workflows:
        return apply_workflow(workflow_result, workflows, part)

    return workflow_result


def part1(workflows, parts):
    total = 0
    for part in parts:
        if apply_workflow('in', workflows, part) == 'A':
            total += sum(part.values())

    return total


def part2(workflows):
    queue = [("in", 0, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})]
    accepted = []

    while queue:
        workflow, index, history = queue.pop()
        if workflow == 'R':
            # print('Rejected:', history)
            continue
        if workflow == 'A':
            accepted.append(history)
            continue
        if index == len(workflows[workflow]) - 1:
            queue.append((workflows[workflow][-1], 0, history))
            continue

        rating_type, condition, value, if_true = workflows[workflow][index]
        # add if true
        history_copy = {k: v.copy() for k, v in history.items()}
        if condition == '<':
            history_copy[rating_type][1] = min(history_copy[rating_type][1], value - 1)
        else:
            history_copy[rating_type][0] = max(history_copy[rating_type][0], value + 1)
        queue.append((if_true, 0, history_copy))

        # add if false
        history_copy = {k: v.copy() for k, v in history.items()}
        if condition == '<':
            history_copy[rating_type][0] = max(history_copy[rating_type][0], value)
        else:
            history_copy[rating_type][1] = min(history_copy[rating_type][1], value)
        queue.append((workflow, index + 1, history_copy))

    total_options = 0
    for accepted_part in accepted:
        total_options += math.prod(interval[1] - interval[0] + 1 for interval in accepted_part.values())
    return total_options


def test():
    sample = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''
    workflows, parts = parse(sample)
    assert part1(workflows, parts) == 19114
    assert part2(workflows) == 167409079868000


test()
data = read_data(2023, 19)
workflows, parts = parse(data)
print('Part1:', part1(workflows, parts))
print('Part2:', part2(workflows))
