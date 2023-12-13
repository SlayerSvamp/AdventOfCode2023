# Day 13: Point of Incidence

name = 'Day 13: Point of Incidence'

part_one_verified = 35210
part_two_verified = 31974


def parse_areas(lines):
    areas = [x.split('\n') for x in ('\n'.join(lines)).split('\n\n')]
    for rows in areas:
        columns = [*map(''.join, zip(*rows))]
        yield rows, columns


def find_reflection_line(sequences, smudge):
    for parting_line in range(1, len(sequences[0])):
        differences = 0
        for sequence in sequences:
            mirrored = sequence[parting_line:]
            mirroring = sequence[parting_line-1::-1]
            differences += sum(x != y for x, y in zip(mirrored, mirroring))
        if smudge == differences:
            return parting_line
    return 0


def total_reflection_lines(lines, diff):
    total = 0
    areas = parse_areas(lines)
    for rows, columns in areas:
        total += find_reflection_line(rows, diff)
        total += find_reflection_line(columns, diff) * 100
    return total


def part_one(lines: list[str]):
    return total_reflection_lines(lines, 0)


def part_two(lines: list[str]):
    return total_reflection_lines(lines, 1)
