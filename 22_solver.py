# Day 22: Sand Slabs

name = 'Day 22: Sand Slabs'

part_one_verified = 401
part_two_verified = 63491


def parse_blocks(lines):
    blocks = []
    for line in lines:
        c1, c2 = sorted(line.split('~'))
        x1, y1, z1 = map(int, c1.split(','))
        x2, y2, z2 = map(int, c2.split(','))
        block = (tuple(sorted((x1, x2))), tuple(
            sorted((y1, y2))), tuple(sorted((z1, z2))))
        blocks.append(block)

    return sorted(blocks, key=lambda x: x[2])


def coordinate_overlap(a, b):
    a1, a2 = a
    b1, b2 = b
    return max(a1, b1) <= min(a2, b2)


def overlaps(block_a, block_b):
    return all(coordinate_overlap(a, b) for a, b in zip(block_a, block_b))


def fall_distance(blocks, block):
    x, y, z = block
    bottom_z = min(z)
    if bottom_z == 1:
        return 0

    support_z = max((0, *(
        bz for bx, by, (_, bz) in blocks
        if bottom_z > bz
        and coordinate_overlap(x, bx)
        and coordinate_overlap(y, by)
    )))
    return max(0, bottom_z - support_z - 1)


def fall(block, distance):
    x, y, (z1, z2) = block
    return x, y, (z1 - distance, z2 - distance)


def supported_by(blocks, block_a):
    fallen_block = fall(block_a, 1)
    supports = set()
    for block_b in blocks:
        if block_a != block_b:
            if overlaps(fallen_block, block_b):
                supports.add(block_b)
    return supports


def settle_blocks(blocks):
    falling = True
    length = len(blocks)
    while falling:
        falling = 0
        for _ in range(length):
            block = blocks.pop(0)
            distance = fall_distance(blocks, block)
            if distance > 0:
                blocks.append(fall(block, distance))
                falling = True
            else:
                blocks.append(block)


def part_one(lines: list[str]):
    blocks = parse_blocks(lines)
    settle_blocks(blocks)
    needed_for_support = set()
    for block in blocks:
        supports = supported_by(blocks, block)
        if len(supports) == 1:
            needed_for_support |= supports

    return len(set(blocks) - needed_for_support)


def part_two(lines: list[str]):
    blocks = parse_blocks(lines)
    settle_blocks(blocks)

    total_removed = 0
    block_supported_by_base = [(x, supported_by(blocks, x)) for x in blocks]
    for block_a in blocks:
        block_supported_by = {k: set(v) for k, v in block_supported_by_base}
        current_removed = [block_a]
        all_removed = 0
        while current_removed:
            next_removed = []
            for removed in current_removed:
                for key, value in block_supported_by.items():
                    if removed in value:
                        value.remove(removed)
                        if not value:
                            next_removed.append(key)
            all_removed += len(next_removed)
            current_removed = next_removed

        total_removed += all_removed
    return total_removed
