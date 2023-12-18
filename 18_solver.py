# Day 18: Lavaduct Lagoon

name = 'Day 18: Lavaduct Lagoon'

part_one_verified = 48795
part_two_verified = None


def ray_casting_inside(vertical, grid):
    [min_x, max_x] = sorted(x for x, _ in grid)[::len(grid)-2]
    [min_y, max_y] = sorted(y for _, y in grid)[::len(grid)-2]
    inside = set()
    for y in range(min_y, max_y + 1):
        isInside = False
        for x in range(min_x, max_x + 1):
            if (x, y) in vertical:
                isInside ^= True
            elif isInside:
                inside.add((x, y))
    return inside


def lagoon_size(instructions):
    x, y = 0, 0
    edge = {(0, 0)}
    vertical = set()

    for direction, steps in instructions:
        dx, dy = 0, 0
        if direction == 'U':
            dy = -1
            vertical.add((x, y))
        elif direction == 'R':
            dx = 1
        if direction == 'D':
            dy = 1
        elif direction == 'L':
            dx = -1
        for _ in range(steps):
            x, y = x+dx, y+dy
            edge.add((x, y))
            if direction in 'UD':
                vertical.add((x, y))
        if direction == 'U':
            vertical.remove((x, y))
    inside = ray_casting_inside(vertical, edge)

    return len(inside | edge)


def part_one(lines: list[str]):
    instructions = []
    for line in lines:
        direction, steps, _ = line.split(' ')
        instructions.append((direction, int(steps)))

    return lagoon_size(instructions)


def part_two(lines: list[str]):
    instructions = []
    for line in lines:
        [*steps_hex, direction_num] = line.split('#')[1][:-1]
        steps = int(''.join(steps_hex), 16)
        direction = 'RDLU'[int(direction_num)]
        instructions.append((direction, steps))
    return lagoon_size(instructions)
