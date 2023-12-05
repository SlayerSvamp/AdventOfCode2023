# Day 5: If You Give A Seed A Fertilizer

name = 'Day 5: If You Give A Seed A Fertilizer'

part_one_verified = 107430936
part_two_verified = None


def parse_maps(lines: list[str]):
    seeds = list(map(int, lines[0].split(': ')[1].split(' ')))
    maps: list[list[tuple[int, int, int]]] = []
    for i in range(1, len(lines)):
        line = lines[i]
        if not line:
            maps.append([])
        elif line.endswith(':'):
            continue
        else:
            maps[-1].append(tuple(map(int, line.split(' '))))
    return seeds, maps


def get_value(item: int, mapping: list[tuple[int, int, int]]):
    for destination, source, length in mapping:
        if item >= source and item <= source + length:
            return item - source + destination
    return item


def overlap_ranges(start, length, cut_start, cut_length, replace_offset):
    if start < cut_start:
        pre_length = max(0, min(cut_start - start, length))
        yield (start, pre_length)
        if pre_length < length:
            length -= pre_length
            start = cut_start
        if length < 1:
            return
    if start > cut_start and cut_start + cut_length > start:
        cut_start, cut_length = start, cut_length - (start - cut_start)
    if start == cut_start:
        yield (cut_start + replace_offset, min(cut_length, length))
        length -= cut_length
        if length < 1:
            return
    if start >= cut_start + cut_length:
        yield (start, length)


def get_ranges(item: tuple[int, int], mapping: list[tuple[int, int, int]]):
    item_start, item_length = item
    for destination, source, map_length in sorted(mapping):
        yield from overlap_ranges(item_start, item_length, source, map_length, destination - source)


def part_one(lines: list[str]):
    sources, maps = parse_maps(lines)
    for _map in maps:
        sources = [get_value(source, _map) for source in sources]
    return min(sources)


def part_two(lines: list[str]):
    sources, maps = parse_maps(lines)
    source_ranges = zip(sources[:-2:2], sources[1::2])
    for _map in maps:
        source_ranges = [
            new_range
            for source_range in source_ranges
            for new_range in get_ranges(source_range, _map)
        ]

    return min(start for start, _ in source_ranges)
