class Instruction:
    def __init__(self, instr_str):
        parts = instr_str.strip().split(" ")
        self.dest = parts[0]
        self.op = parts[1]
        self.by = int(parts[2])
        self.left_comp = parts[4]
        self.comp = parts[5]
        self.right_comp = int(parts[6])

    def __str__(self):
        return (
            "dest:"
            + self.dest
            + " op:"
            + self.op
            + " by:"
            + str(self.by)
            + " l:"
            + self.left_comp
            + " comp:"
            + self.comp
            + " r:"
            + str(self.right_comp)
        )
