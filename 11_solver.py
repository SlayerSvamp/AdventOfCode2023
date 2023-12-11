# Day 11: Cosmic Expansion

name = 'Day 11: Cosmic Expansion'

part_one_verified = 9965032
part_two_verified = 550358864332


def sum_galaxy_pair_distances(lines, expansion_factor):
    space = set()
    populated_x = set(x for x, c in enumerate(zip(*lines)) if '#' in c)
    populated_y = set(y for y, c in enumerate(lines) if '#' in c)
    empty_y = 0
    for y, line in enumerate(lines):
        if y not in populated_y:
            empty_y += 1
        empty_x = 0
        for x, c in enumerate(line):
            if x not in populated_x:
                empty_x += 1
            elif c == '#':
                space.add((
                    x + empty_x * (expansion_factor - 1),
                    y + empty_y * (expansion_factor - 1)
                ))

    return sum(
        abs(x1 - x2) + abs(y1 - y2)
        for x1, y1 in space
        for x2, y2 in space
    ) // 2


def part_one(lines: list[str]):
    return sum_galaxy_pair_distances(lines, 2)


def part_two(lines: list[str], expansion_factor=1000_000):
    return sum_galaxy_pair_distances(lines, expansion_factor)
