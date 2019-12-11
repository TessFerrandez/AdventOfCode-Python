def sum_of_sequence(sequence, step=1):
    sequence_len = len(sequence)
    sequence_sum = 0
    for index in range(sequence_len):
        if sequence[index] == sequence[(index + step) % sequence_len]:
            sequence_sum += int(sequence[index])
    return sequence_sum


def puzzles():
    sequence = open('input/day1.txt').readline()
    print("captcha:", sum_of_sequence(sequence))
    print("captcha:", sum_of_sequence(sequence, len(sequence) // 2))


if __name__ == "__main__":
    puzzles()
