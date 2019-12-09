from IntCode import IntCode, OutputInterrupt


def puzzle1():
    computer = IntCode(open('input/day9.txt').readline())
    computer.input_queue.append(1)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            print("BOOST code: ", computer.output_queue[-1])


def puzzle2():
    computer = IntCode(open('input/day9.txt').readline())
    computer.input_queue.append(2)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            print("Sensor BOOST code: ", computer.output_queue[-1])


if __name__ == "__main__":
    puzzle1()
    puzzle2()
