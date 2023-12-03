# Day 3: Gear Ratios

name = 'Day 3: Gear Ratios'

part_one_verified = 535235
part_two_verified = 79844424


def neighbours(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx or dy:
                yield x + dx, y + dy


def parse_schematics(lines):
    symbols = dict()
    parts = []
    value = ''
    coords = []

    def is_part(coords):
        for x, y in coords:
            for key in neighbours(x, y):
                if key in symbols:
                    return True
    grid = [
        ((x, y), c)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
    ]

    for key, c in grid:
        if c not in '.0123456789':
            symbols[key] = c

    for key, c in grid:
        if c.isnumeric():
            value += c
            coords.append(key)
        elif value:
            if is_part(coords):
                parts.append((int(value), coords))
            value = ''
            coords = []

    return parts, symbols


def part_one(lines: list[str]):
    parts, _ = parse_schematics(lines)
    return sum(value for value, _ in parts)


def part_two(lines: list[str]):
    parts, symbols = parse_schematics(lines)

    def part_is_close(x, y, part):
        for key in part:
            if key in neighbours(x, y):
                return True

    gear_ratios = 0
    for x, y in symbols:
        if symbols[x, y] == '*':
            adjacent = []
            for value, coords in parts:
                if part_is_close(x, y, coords):
                    adjacent.append(value)
            if len(adjacent) == 2:
                a, b = adjacent
                gear_ratios += a * b

    return gear_ratios
