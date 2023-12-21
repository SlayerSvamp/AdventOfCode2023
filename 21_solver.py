# Day 21: Step Counter

name = 'Day 21: Step Counter'

part_one_verified = 3858
part_two_verified = None

directions = ((0, 1), (1, 0), (-1, 0), (0, -1))


def adjacent(plots, plot, wrap_size):
    x, y = plot
    if wrap_size:
        wx, wy = wrap_size or (0, 0)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (nx % wx, ny % wy) in plots:
                yield nx, ny
    else:
        for dx, dy in directions:
            adj = x+dx, y+dy
            if adj in plots:
                yield adj


def parse_garden(lines):
    return {
        (x, y): tile
        for y, line in enumerate(lines)
        for x, tile in enumerate(line)
        if tile in '.S'
    }


def get_final_plots(plots, steps, wrap_size):
    available = {key for key in plots if plots[key] == 'S'}
    prev_prev_odd = set()
    prev_prev_even = set()
    prev_odd = set()
    prev_even = set(available)
    odd = 0
    even = 1
    for step in range(1, steps+1):
        available = {
            adj
            for plot in available
            for adj in adjacent(plots, plot, wrap_size)
        }
        if step % 2:
            available -= prev_even | prev_prev_even
            prev_prev_even = prev_even
            prev_even = available
            even += len(available)
        else:
            available -= prev_odd | prev_prev_odd
            prev_prev_odd = prev_odd
            prev_odd = available
            odd += len(available)

    return (even if steps % 2 else odd)


def part_one(lines: list[str], steps=64):
    plots = parse_garden(lines)
    return get_final_plots(plots, steps, False)


def part_two(lines: list[str], steps=26501365):
    plots = parse_garden(lines)
    return get_final_plots(plots, steps, (len(lines[0]), len(lines)))
