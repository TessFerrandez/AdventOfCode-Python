from typing import Tuple


def read_input() -> str:
    hex_val = open('2021/input/day16.txt').read().strip()
    return bin(int(hex_val, 16))[2:].zfill(len(hex_val) * 4)


def read_version(message: str) -> Tuple[int, str]:
    return int(message[:3], 2), message[3:]


def read_type(message: str) -> Tuple[int, str]:
    return int(message[:3], 2), message[3:]


def read_literals(message: str) -> Tuple[int, str]:
    go_on, chunk = message[0], message[1: 5]
    literal = chunk
    read = 5
    message = message[5:]

    while go_on != "0":
        go_on, chunk = message[0], message[1: 5]
        literal += chunk
        read += 5
        message = message[5:]

    return int(literal, 2), message


def read_message_length(message, num_bits_to_read) -> Tuple[int, str]:
    num_bits = int(message[:num_bits_to_read], 2)
    message = message[num_bits_to_read:]
    return num_bits, message


def process_bits(message, num_bits, indent) -> Tuple[int, str]:
    message_to_process = message[:num_bits]
    sum_versions = 0

    while len(message_to_process) > 0:
        version_sum, message_to_process = process_message(message_to_process, indent)
        sum_versions += version_sum

    return sum_versions, message[num_bits:]


def process_messages(message, num_messages, indent) -> Tuple[int, str]:
    sum_versions = 0

    for _ in range(num_messages):
        version_sum, message = process_message(message, indent)
        sum_versions += version_sum

    return sum_versions, message


def process_message(message: str, indent="") -> Tuple[int, str]:
    sum_versions = 0

    print(f"{indent}------------")

    # read version
    version, message = read_version(message)
    sum_versions += version
    print(f"{indent}VERSION: {version}")

    # read type
    type, message = read_type(message)
    print(f"{indent}TYPE: {type}")

    if type == 4:
        literal, message = read_literals(message)
        print(f"{indent}LITERALS: {literal}")
    elif message[0] == "0":
        num_bits, message = read_message_length(message[1:], 15)
        version_sum, message = process_bits(message, num_bits, indent + "  ")
        sum_versions += version_sum
    else:
        num_messages, message = read_message_length(message[1:], 11)
        version_sum, message = process_messages(message, num_messages, indent + "  ")
        sum_versions += version_sum

    return sum_versions, message


message = read_input()
versions, message = process_message(message)

print("------------")
print("Part 1:", versions)
