import re
import pytest
from typing import List


@pytest.mark.parametrize('data, expected',
                         [
                             ('20x3x11', [20, 3, 11]),
                         ])
def test_extract_numbers(data: str, expected: List[int]):
    assert extract_numbers(data) == expected


def extract_numbers(data: str) -> List[int]:
    return list(map(int, re.findall(r'[-\d]+', data)))


def parenthetic_contents(expression: str) -> (int, str):
    """
    generate parenthesized content in string as pairs (level, contents)
    """
    stack = []
    for i, c in enumerate(expression):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield len(stack), expression[start + 1: i]
