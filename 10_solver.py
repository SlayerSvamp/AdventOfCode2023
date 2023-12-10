# Day 10: Pipe Maze

name = 'Day 10: Pipe Maze'

part_one_verified = 7102
part_two_verified = 363

direction_shapes = ['7|F', 'J-7', 'L|J', 'F-L']
direction_coordinates = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse_maze(lines):
    maze = {
        (x, y): c
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
    }
    start = next(xy for xy, c in maze.items() if c == 'S')
    return maze, start


def get_starting_direction(maze, x, y):
    for direction, acceptable in enumerate(direction_shapes):
        dx, dy = direction_coordinates[direction]
        pos = (x + dx, y + dy)
        if pos in maze and maze[pos] in acceptable:
            return direction


def find_loop(lines):
    maze, (x, y) = parse_maze(lines)
    direction = get_starting_direction(maze, x, y)
    loop = set()
    left_side = set()
    right_side = set()
    total_turn = 0

    while True:
        loop.add((x, y))
        coordinates = direction_coordinates[direction]
        side_dx = (1, 0, -1, 0)[direction]
        side_dy = (0, 1, 0, -1)[direction]
        for dx, dy in [(0, 0), coordinates]:
            x, y = x + dx, y + dy
            left_side.add((x - side_dx, y - side_dy))
            right_side.add((x + side_dx, y + side_dy))

        pipe = maze[x, y]

        if pipe == 'S':
            enclosed = left_side if total_turn < 0 else right_side
            return loop, enclosed - loop

        turn = direction_shapes[direction].index(pipe) - 1
        total_turn += turn
        direction += 4 + turn
        direction %= 4


def part_one(lines: list[str]):
    loop, _ = find_loop(lines)
    return len(loop) // 2


def adjacent(x, y):
    return {
        (x+dx, y+dy)
        for dy in [-1, 0, 1]
        for dx in [-1, 0, 1]
        if dx or dy
    }


def part_two(lines: list[str]):
    loop, enclosed = find_loop(lines)
    current = enclosed
    while current:
        current = {adj for x, y in current for adj in adjacent(x, y)}
        current -= enclosed | loop
        enclosed |= current
    return len(enclosed)
