# Day 14: Parabolic Reflector Dish

name = 'Day 14: Parabolic Reflector Dish'

part_one_verified = 106517
part_two_verified = 79723


def parse_platform(lines):
    north = len(lines) + 1
    east = len(lines[0]) + 1
    north_edge = set((x, north) for x in range(east))
    south_edge = set((x, 0) for x in range(east))
    west_edge = set((0, y) for y in range(north))
    east_edge = set((east, y) for y in range(north))
    rounded_rocks = set()
    cube_shaped_rocks = set()
    for i, line in enumerate(lines):
        y = len(lines) - i
        for j, c in enumerate(line):
            x = j + 1
            if c == '#':
                cube_shaped_rocks.add((x, y))
            if c == 'O':
                rounded_rocks.add((x, y))
    obstacles = cube_shaped_rocks
    obstacles |= north_edge | south_edge | west_edge | east_edge
    return obstacles, rounded_rocks


def tilt_platform(obstacles, rounded_rocks, direction):
    dx, dy = direction
    any_rock_rolled = True
    while any_rock_rolled:
        any_rock_rolled = False
        for x, y in list(rounded_rocks):
            rock_rolled = False
            rolled = (rx, ry) = (x+dx, y+dy)
            while rolled not in obstacles and rolled not in rounded_rocks:
                rolled = (rx, ry) = (rx+dx, ry+dy)
                rock_rolled = True
            if rock_rolled:
                rounded_rocks.remove((x, y))
                rounded_rocks.add((rx-dx, ry-dy))
                any_rock_rolled = True


def part_one(lines: list[str]):
    obstacles, rounded_rocks = parse_platform(lines)
    tilt_platform(obstacles, rounded_rocks, (0, 1))
    return sum(y for _, y in rounded_rocks)


def part_two(lines: list[str]):
    obstacles, rounded_rocks = parse_platform(lines)
    rock_history = []
    current = tuple(sorted(rounded_rocks))
    while current not in rock_history:
        rock_history.append(current)
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            tilt_platform(obstacles, rounded_rocks, direction)
        current = tuple(sorted(rounded_rocks))

    loop_start = rock_history.index(current)
    loop_length = len(rock_history) - loop_start
    cycles_left = 1000_000_000 - len(rock_history)
    cycles_left %= loop_length

    final_rocks = rock_history[loop_start + cycles_left]
    return sum(y for _, y in final_rocks)
