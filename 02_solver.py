# Day 2: Cube Conundrum

name = 'Day 2: Cube Conundrum'

part_one_verified = 2085
part_two_verified = 79315


def parse_games(lines: str):
    for line in lines:
        [game_raw, sets] = line.split(': ')
        game = int(game_raw.split(' ')[1])
        pairs = [
            (int(n), color)
            for set in sets.split('; ')
            for n, color in [
                pair.split(' ')
                for pair in set.split(', ')
            ]
        ]
        yield game, pairs


def part_one(lines: list[str]):
    limit = {'red': 12, 'green': 13, 'blue': 14}
    return sum(
        game for game, pairs in parse_games(lines)
        if not sum(
            int(n) > limit[color]
            for n, color in pairs
        )
    )


def part_two(lines: list[str]):
    return sum(
        max(n for n, color in pairs if color == 'red')
        * max(n for n, color in pairs if color == 'green')
        * max(n for n, color in pairs if color == 'blue')
        for _, pairs in parse_games(lines)
    )
