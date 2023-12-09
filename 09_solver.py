# Day 9: Mirage Maintenance

name = 'Day 9: Mirage Maintenance'

part_one_verified = 1916822650
part_two_verified = 966


def parse_history(lines):
    return [
        [int(x) for x in line.split(' ')]
        for line in lines
    ]


def extrapolate(values: list[int]):
    differences = [b-a for a, b in zip(values, values[1:])]
    previous_value = values[0]
    next_value = values[-1]
    if any(differences):
        first_diff, last_diff = extrapolate(differences)
        previous_value -= first_diff
        next_value += last_diff
    return previous_value, next_value


def part_one(lines: list[str]):
    return sum(extrapolate(sequence)[1] for sequence in parse_history(lines))


def part_two(lines: list[str]):
    return sum(extrapolate(sequence)[0] for sequence in parse_history(lines))
