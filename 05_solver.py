# Day 5: If You Give A Seed A Fertilizer

name = 'Day 5: If You Give A Seed A Fertilizer'

part_one_verified = 107430936
part_two_verified = 23738616


def parse_almanac(lines: list[str]):
    seeds = list(map(int, lines[0].split(': ')[1].split(' ')))
    category_maps: list[list[tuple[int, int, int]]] = []
    for i in range(1, len(lines)):
        line = lines[i]
        if not line:
            category_maps.append([])
        elif not line.endswith(':'):
            destination, source, length = map(int, line.split(' '))
            source_end = source + length - 1
            map_diff = destination - source
            category_maps[-1].append((source, source_end, map_diff))
    return seeds, category_maps


def part_one(lines: list[str]):
    items, category_maps = parse_almanac(lines)
    for category_map in category_maps:
        next_items = []
        for item in items:
            for source, source_end, map_diff in category_map:
                if item >= source and item <= source_end:
                    next_items.append(item + map_diff)
                    break
            else:
                next_items.append(item)
        items = next_items
    return min(items)


def part_two(lines: list[str]):
    seeds, category_maps = parse_almanac(lines)
    source_ranges = [
        (start, start + length - 1)
        for start, length in zip(seeds[::2], seeds[1::2])
    ]
    for category_map in category_maps:
        next_ranges = set()
        for start, end in source_ranges:
            for source, source_end, map_diff in sorted(category_map):
                if start < source:
                    next_ranges.add((start, min(end, source - 1)))

                if end >= source and start <= source_end:
                    next_ranges.add((
                        max(start, source) + map_diff,
                        min(end, source_end) + map_diff
                    ))

                if end > source_end:
                    start = max(start, source_end + 1)
                else:
                    break
            else:
                next_ranges.add((start, end))

        source_ranges = next_ranges

    return min(start for start, _ in source_ranges)
