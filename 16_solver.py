# Day 16: The Floor Will Be Lava

name = 'Day 16: The Floor Will Be Lava'

part_one_verified = 7074
part_two_verified = 7530


def count_energized_tiles(contraption, start):
    out_of_bounds_x = (-1, len(contraption[0]))
    out_of_bounds_y = (-1, len(contraption))
    rays = {start}
    traced_rays = {start}

    def add_ray(x, y, direction):
        if direction == 'up':
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        if x not in out_of_bounds_x and y not in out_of_bounds_y:
            ray = x, y, direction
            if ray not in rays:
                rays.add(ray)
                traced_rays.add(ray)

    while traced_rays:
        x, y, direction = traced_rays.pop()
        tile = contraption[y][x]
        if direction == 'up':
            if tile in '|.':
                add_ray(x, y, 'up')
            else:
                if tile in '/-':
                    add_ray(x, y, 'right')
                if tile in '\-':
                    add_ray(x, y, 'left')
        elif direction == 'right':
            if tile in '-.':
                add_ray(x, y, 'right')
            else:
                if tile in '/|':
                    add_ray(x, y, 'up')
                if tile in '\|':
                    add_ray(x, y, 'down')
        elif direction == 'down':
            if tile in '|.':
                add_ray(x, y, 'down')
            else:
                if tile in '\-':
                    add_ray(x, y, 'right')
                if tile in '/-':
                    add_ray(x, y, 'left')
        elif direction == 'left':
            if tile in '-.':
                add_ray(x, y, 'left')
            else:
                if tile in '\|':
                    add_ray(x, y, 'up')
                if tile in '/|':
                    add_ray(x, y, 'down')

    return len({(x, y) for x, y, _ in rays})


def part_one(lines: list[str]):
    return count_energized_tiles(lines, (0, 0, 'right'))


def part_two(lines: list[str]):
    starts = []
    for x in range(len(lines[0])):
        starts.append((x, 0, 'down'))
        starts.append((x, len(lines) - 1, 'up'))
    for y in range(len(lines)):
        starts.append((0, y, 'right'))
        starts.append((len(lines[0]) - 1, y, 'left'))
    return max(count_energized_tiles(lines, start) for start in starts)
