# Day 18: Lavaduct Lagoon

name = 'Day 18: Lavaduct Lagoon'


part_one_verified = 48795
part_two_verified = 40654918441248


def shoelace_formula(coordinates):
    zipped = list(zip(coordinates[:], coordinates[1:]))
    return abs(sum(
        (x1*y2) - (x2*y1)
        for (x1, y1), (x2, y2) in zipped
    )) // 2


def lagoon_size(instructions):
    direction_coordinates = {
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0),
        'U': (0, -1),
    }
    coordinates = [(x, y)] = [(0, 0)]
    for direction, meters in instructions:
        dx, dy = direction_coordinates[direction]
        x = x + dx * meters
        y = y + dy * meters
        coordinates.append((x, y))
    area = shoelace_formula(coordinates)
    trench_meters = sum(meters for _, meters in instructions)
    trench_outside_area = trench_meters // 2 + 1
    return area + trench_outside_area


def part_one(lines: list[str]):
    instructions = []
    for line in lines:
        direction, meters = line.split(' ')[:2]
        instructions.append((direction, int(meters)))
    return lagoon_size(instructions)


def part_two(lines: list[str]):
    correct_instructions = []
    for line in lines:
        hex = line[:-1].split('#')[1]
        meters = int(''.join(hex[:-1]), 16)
        direction = 'RDLU'[int(hex[-1])]
        correct_instructions.append((direction, meters))
    return lagoon_size(correct_instructions)
