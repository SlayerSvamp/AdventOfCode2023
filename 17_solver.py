# Day 17: Clumsy Crucible

name = 'Day 17: Clumsy Crucible'

part_one_verified = 767
part_two_verified = 904


def parse_heat_loss_map(lines):
    return {
        (x, y): int(c)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
    }


direction_coords = {
    'up': (0, -1),
    'right': (1, 0),
    'down': (0, 1),
    'left': (-1, 0),
}


def lowest_heat_loss(lines, min_consecutive_blocks, wobbly_limit):
    heat_loss_map = parse_heat_loss_map(lines)
    lava_pool = min(heat_loss_map)
    machine_parts_factory = max(heat_loss_map)
    observed = [
        (0, *lava_pool, 'down', 1),
        (0, *lava_pool, 'right', 1),
    ]

    already_tested = {}
    lowest_heat_loss = None
    while len(observed):
        next_observed = []
        for heat_loss, x, y, direction, consecutive_blocks in observed:
            candidates = []
            if consecutive_blocks >= min_consecutive_blocks:
                if direction in ('left', 'right'):
                    candidates.append(('up', 1))
                    candidates.append(('down', 1))
                elif direction in ('up', 'down'):
                    candidates.append(('left', 1))
                    candidates.append(('right', 1))
            if consecutive_blocks < wobbly_limit:
                candidates.append((direction, consecutive_blocks + 1))

            for next_direction, next_consecutive_blocks in candidates:
                dx, dy = direction_coords[direction]
                next_coords = x + dx, y + dy
                if next_coords in heat_loss_map:
                    next_heat_loss = heat_loss + heat_loss_map[next_coords]
                    if next_coords == machine_parts_factory:
                        if not lowest_heat_loss or next_heat_loss < lowest_heat_loss:
                            if consecutive_blocks >= min_consecutive_blocks:
                                lowest_heat_loss = next_heat_loss
                    key = *next_coords, next_direction, next_consecutive_blocks
                    if key not in already_tested or already_tested[key] > next_heat_loss:
                        next_observed.append((next_heat_loss, *key))
                        already_tested[key] = next_heat_loss

        observed = sorted(
            (h, x, y, d, s)
            for h, x, y, d, s in next_observed
            if not lowest_heat_loss or h <= lowest_heat_loss
        )
    return lowest_heat_loss


def part_one(lines: list[str]):
    return lowest_heat_loss(lines, 0, 3)


def part_two(lines: list[str]):
    return lowest_heat_loss(lines, 4, 10)
