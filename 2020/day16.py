from typing import List, Tuple


def parse_input(filename: str) -> Tuple[dict, List[int], List[List[int]]]:
    rules_info, ticket_info, nearby_info = open(filename).read().strip().split('\n\n')

    rules = {}
    rule_strings = [rule for rule in rules_info.split('\n')]
    for rule in rule_strings:
        field, conditions = rule.split(': ')
        conditions = conditions.split(' or ')
        rules[field] = [[int(val) for val in condition.split('-')] for condition in conditions]

    my_ticket = [int(val) for val in ticket_info.split('\n')[1].split(',')]

    nearby = []
    for ticket in nearby_info.split('\n')[1:]:
        nearby.append([int(val) for val in ticket.split(',')])

    return rules, my_ticket, nearby


def get_all_conditions(rules: dict) -> List[List[int]]:
    all_conditions = []
    for rule in rules:
        all_conditions += rules[rule]
    return all_conditions


def is_valid(value: int, conditions: List[List[int]]) -> bool:
    for condition in conditions:
        c1, c2 = condition
        if c1 <= value <= c2:
            return True
    return False


def part1(rules: dict, nearby: List[List[int]]) -> int:
    conditions = get_all_conditions(rules)

    invalid = []
    for ticket in nearby:
        for digit in ticket:
            if not is_valid(digit, conditions):
                invalid.append(digit)
    return sum(invalid)


def remove_invalid_tickets(rules: dict, nearby: List[List[int]]):
    conditions = get_all_conditions(rules)

    tickets_to_remove = []
    for ticket in nearby:
        for digit in ticket:
            if not is_valid(digit, conditions):
                tickets_to_remove.append(ticket)
                break

    for ticket in tickets_to_remove:
        nearby.remove(ticket)


def get_valid_rules_by_position(rules: dict, nearby: List[List[int]], ticket: List[int]) -> dict:
    valid_rules = {}

    num_fields = len(ticket)
    for i in range(num_fields):
        possible_rules = list(rules.keys())
        rules_to_remove = []
        for rule in possible_rules:
            for ticket in nearby:
                value = ticket[i]
                c1, c2 = rules[rule][0]
                c3, c4 = rules[rule][1]
                if not(c1 <= value <= c2 or c3 <= value <= c4):
                    rules_to_remove.append(rule)
                    break
        for rule in rules_to_remove:
            possible_rules.remove(rule)
        valid_rules[i] = possible_rules
    return valid_rules


def map_field_to_position(valid_rules: dict) -> dict:
    field_map = {}

    while valid_rules:
        positions_with_one_valid_rule = [position for position in valid_rules if len(valid_rules[position]) == 1]
        for position in positions_with_one_valid_rule:
            field = valid_rules[position][0]
            field_map[position] = field
            del valid_rules[position]
            for rule in valid_rules:
                if field in valid_rules[rule]:
                    valid_rules[rule].remove(field)
    return field_map


def part2(rules: dict, nearby: List[List[int]], ticket: List[int]) -> int:
    # map columns to fields
    remove_invalid_tickets(rules, nearby)
    valid_rules = get_valid_rules_by_position(rules, nearby, ticket)
    field_map = map_field_to_position(valid_rules)

    # calculate the product of the departure fields in my ticket
    positions = [position for position in field_map if 'departure' in field_map[position]]
    result = 1
    for position in positions:
        result *= ticket[position]

    return result


def main():
    rules, ticket, nearby = parse_input('input/day16.txt')
    print(f'Part 1: {part1(rules, nearby)}')
    print(f'Part 2: {part2(rules, nearby, ticket)}')


if __name__ == "__main__":
    main()
