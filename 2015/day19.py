def get_molecules(transformation: list, original: str) -> list:
    from_str = transformation[0]
    to_str = transformation[1]
    repl_length = len(from_str)

    molecules = []
    for i in range(len(original) - repl_length + 1):
        if original[i : i + repl_length] == from_str:
            molecules.append(original[:i] + to_str + original[i + repl_length :])

    return molecules


def replace_and_count(original: str, repl: str) -> (str, int):
    len_before = len(original)
    replaced = original.replace(repl, "X")
    len_after = len(replaced)
    while len_before != len_after:
        len_before = len(replaced)
        replaced = replaced.replace(repl, "X")
        len_after = len(replaced)
    return replaced, (len(original) - len(replaced)) // (len(repl) - 1)


def get_steps_to_create_molecule(original: str) -> int:
    replaced = (
        original.replace("Rn", "(")
        .replace("Y", ",")
        .replace("Ar", ")")
        .replace("Al", "X")
        .replace("B", "X")
        .replace("Ca", "X")
        .replace("C", "X")
        .replace("F", "X")
        .replace("H", "X")
        .replace("H", "X")
        .replace("Mg", "X")
        .replace("N", "X")
        .replace("O", "X")
        .replace("P", "X")
        .replace("Si", "X")
        .replace("Th", "X")
        .replace("Ti", "X")
    )

    steps = 0
    while True:
        replaced, count = replace_and_count(replaced, "XX")
        if count > 0:
            steps += count
            continue
        replaced, count = replace_and_count(replaced, "X(X)")
        if count > 0:
            steps += count
            continue
        replaced, count = replace_and_count(replaced, "X(X,X)")
        if count > 0:
            steps += count
            continue
        break

    return steps


def puzzles():
    transformations = [line.strip().split(" => ") for line in open("input/day19.txt")]
    molecules = []
    original = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
    for transformation in transformations:
        molecules += get_molecules(transformation, original)
    print("num molecules", len(set(molecules)))

    steps = get_steps_to_create_molecule(original)
    print(steps, "steps to molecule")


if __name__ == "__main__":
    puzzles()
