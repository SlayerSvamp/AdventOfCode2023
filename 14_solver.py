# Day 14: Parabolic Reflector Dish

name = 'Day 14: Parabolic Reflector Dish'

part_one_verified = 106517
part_two_verified = None


def parse_field(lines):
    square_stones = set()
    rolling_stones = set()
    for i, line in enumerate(lines):
        y = len(lines) - i
        for j, c in enumerate(line):
            x = j + 1
            if c == '#':
                square_stones.add((x, y))
            if c == 'O':
                rolling_stones.add((x, y))
    bounds = len(lines[0]), len(lines)
    return square_stones, rolling_stones, bounds


def move_stones(square_stones, rolling_stones, bounds, direction):
    bx, by = bounds
    while True:
        moved = False
        for old in list(rolling_stones):
            new = tuple(map(sum, zip(old, direction)))
            nx, ny = new
            if new not in square_stones \
                and new not in rolling_stones \
                    and ny <= by and ny > 0 and nx <= bx and nx > 0:
                rolling_stones.remove(old)
                rolling_stones.add(new)
                moved = True
        if not moved:
            break


def part_one(lines: list[str]):
    square_stones, rolling_stones, bounds = parse_field(lines)
    move_stones(square_stones, rolling_stones, bounds, (0, 1))
    return sum(y for _, y in rolling_stones)


def part_two(lines: list[str]):
    goal_cycles = 1000_000_000
    square_stones, rolling_stones, bounds = parse_field(lines)
    seen = set()
    seen_list = []
    current = tuple(sorted(rolling_stones))
    seen.add(current)
    seen_list.append(current)
    while True:
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            move_stones(square_stones, rolling_stones, bounds, direction)
        current = tuple(sorted(rolling_stones))
        if current in seen:
            break
        seen.add(current)
        seen_list.append(current)

    loop_start = seen_list.index(current)
    loop_length = len(seen_list) - loop_start
    print()
    print(loop_start)
    print(loop_length)
    cycles_left = goal_cycles - len(seen_list)
    cycles_left %= loop_length

    final_stones = seen_list[loop_start + cycles_left]
    # 79714 too low
    return sum(y for _, y in final_stones)
