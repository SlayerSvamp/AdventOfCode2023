# Day 21: Step Counter

name = 'Day 21: Step Counter'

part_one_verified = 3858
part_two_verified = 636350496972143
directions = ((0, 1), (1, 0), (-1, 0), (0, -1))


def parse_garden(lines):
    return {
        (x, y): tile
        for y, line in enumerate(lines)
        for x, tile in enumerate(line)
        if tile in '.S'
    }


def adjacent(plots, plot):
    x, y = plot
    for dx, dy in directions:
        adj = x+dx, y+dy
        if adj in plots:
            yield adj


def get_garden_progression(plots):
    def inner():
        available = {c for c in plots if plots[c] == 'S'}
        odd = set()
        even = set()
        step = 0
        while available:
            if step % 2:
                odd |= available
                yield len(odd)
            else:
                even |= available
                yield len(even)

            step += 1
            available = {
                adj
                for plot in available
                for adj in adjacent(plots, plot)
                if (adj not in odd) and (adj not in even)
            }
    return list(inner())


def part_one(lines: list[str], steps=64):
    plots = parse_garden(lines)
    progression = get_garden_progression(plots)
    return progression[steps]


def part_two(lines: list[str], steps=26501365):
    plots = parse_garden(lines)
    width = len(lines)
    n = steps // width
    progression = get_garden_progression(plots)
    odd = progression[1::2][-1]
    even = progression[::2][-1]
    odd_diamond = progression[width // 2]
    even_diamond = progression[width // 2 - 1]
    even_hollow = even - even_diamond

    return odd*n*(n+1) + even*n*n + odd_diamond*(n+1) + even_hollow*n
