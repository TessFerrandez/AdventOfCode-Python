from input_processing import read_data


def parse_line(line):
    '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'''
    piles = [pile.split(', ') for pile in line.split(': ')[1].split('; ')]
    options = [{pick.split(' ')[1]: int(pick.split(' ')[0]) for pick in pile} for pile in piles]
    return options


def get_max_cubes(game):
    return {
        'green': max(pick['green'] for pick in game if 'green' in pick),
        'blue': max(pick['blue'] for pick in game if 'blue' in pick),
        'red': max(pick['red'] for pick in game if 'red' in pick)
    }


def parse(data):
    games = [parse_line(line) for line in data.splitlines()]
    return [get_max_cubes(game) for game in games]


def part1(games):
    return sum(i + 1 for i, game in enumerate(games) if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14)


def part2(games):
    return sum(game['red'] * game['green'] * game['blue'] for game in games)


def test():
    sample = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    assert part1(parse(sample)) == 8
    assert part2(parse(sample)) == 2286


test()
data = read_data(2023, 2)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
