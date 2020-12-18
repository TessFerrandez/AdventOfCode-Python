import pytest
from typing import List


@pytest.mark.parametrize('expression, expected',
                         [
                             ('1 + 2 * 3 + 4 * 5 + 6', 71),
                             ('1 + (2 * 3) + (4 * (5 + 6))', 51),
                             ('2 * 3 + (4 * 5)', 26),
                             ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
                             ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
                             ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
                         ])
def test_evaluate(expression: str, expected: int):
    assert evaluate(expression) == expected


@pytest.mark.parametrize('expression, expected',
                         [
                             ('1 + 2 * 3 + 4 * 5 + 6', 231),
                             ('1 + (2 * 3) + (4 * (5 + 6))', 51),
                             ('2 * 3 + (4 * 5)', 46),
                             ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
                             ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
                             ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
                         ])
def test_evaluate_advanced(expression: str, expected: int):
    assert evaluate_advanced(expression) == expected


def get_inner_parenthesis_content(expression: str) -> str:
    """
    returns the innermost parenthesis - e.g. ((5 + 2 + (3 * 2)) + (2 + 3))
    would return (3 * 2)
    -- note, other lower may exist later in the string but this is the first
    -- occurring leaf node
    :param expression: string with math equation
    :return: contents of lowest level parenthesis
    """
    stack = []
    for i, c in enumerate(expression):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            return expression[start + 1: i]
    return ''


def evaluate(expression_str: str) -> int:
    # reduce all parenthesis to their values
    # starting with the ones that have no nested parenthesis inside
    # until we have an expression with only numbers
    while '(' in expression_str:
        content = get_inner_parenthesis_content(expression_str)
        result = evaluate(content)
        expression_str = expression_str.replace('(' + content + ')', str(result))

    # now we have an expression with no parenthesis
    # - so we can cleanly calculate it
    expression = expression_str.split(' ')
    if expression:
        mem = int(expression.pop(0))
        while expression:
            op = expression.pop(0)
            value = int(expression.pop(0))
            if op == '+':
                mem += value
            elif op == '*':
                mem *= value
        return mem
    else:
        return 0


def evaluate_advanced(expression_str: str) -> int:
    # reduce all parenthesis to their values
    # starting with the ones that have no nested parenthesis inside
    # until we have an expression with only numbers
    while '(' in expression_str:
        content = get_inner_parenthesis_content(expression_str)
        result = evaluate_advanced(content)
        expression_str = expression_str.replace('(' + content + ')', str(result))

    expression = expression_str.split(' ')

    # reduce the + first
    while True:
        try:
            pos = expression.index('+')
            value = int(expression[pos - 1]) + int(expression[pos + 1])
            expression = expression[: pos - 1] + [str(value)] + expression[pos + 2:]
        except ValueError:
            break

    # now we have an expression only multiplication
    # - so we can cleanly calculate it
    if expression:
        mem = int(expression.pop(0))
        while expression:
            _ = expression.pop(0)
            value = int(expression.pop(0))
            mem *= value
        return mem
    else:
        return 0


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(expressions: List[str]) -> int:
    return sum(evaluate(expression) for expression in expressions)


def part2(expressions: List[str]) -> int:
    return sum(evaluate_advanced(expression) for expression in expressions)


def main():
    expressions = parse_input('input/day18.txt')
    print(f'Part 1: {part1(expressions)}')
    print(f'Part 2: {part2(expressions)}')


if __name__ == '__main__':
    main()
