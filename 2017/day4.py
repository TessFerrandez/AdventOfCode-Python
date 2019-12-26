def has_dupe_words(pass_phrase):
    for i in range(len(pass_phrase)):
        if pass_phrase[i] in pass_phrase[i + 1 :]:
            return True
    return False


def has_anagram_words(pass_phrase: list) -> bool:
    for i in range(len(pass_phrase)):
        current = sorted(pass_phrase[i])
        for j in range(i + 1, len(pass_phrase)):
            if current == sorted(pass_phrase[j]):
                return True
    return False


def puzzles():
    pass_phrases = [
        [word for word in line.strip().split(" ")]
        for line in open("input/day4.txt").readlines()
    ]
    print(
        "valid phrases:",
        sum(0 if has_dupe_words(pass_phrase) else 1 for pass_phrase in pass_phrases),
    )
    print(
        "valid phrases:",
        sum(0 if has_anagram_words(pass_phrase) else 1 for pass_phrase in pass_phrases),
    )


if __name__ == "__main__":
    puzzles()
