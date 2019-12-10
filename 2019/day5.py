"""
IntCode computer - Part II
"""
from IntCode import IntCode, OutputInterrupt


def get_last_output(input_number):
    computer = IntCode(open('input/day5.txt').readline())
    computer.input_queue.append(input_number)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            diagnostics = computer.output_queue[-1]
    print("diagnostics:", diagnostics)


def puzzle1and2():
    get_last_output(1)
    get_last_output(5)


if __name__ == "__main__":
    puzzle1and2()
