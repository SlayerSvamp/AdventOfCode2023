# Day 12: Hot Springs

name = 'Day 12: Hot Springs'

part_one_verified = 7163
part_two_verified = 17788038834112


def parse_record(line: str, unfold: bool):
    conditions, groups = line.split(' ')
    groups = [int(n) for n in groups.split(',')]
    if unfold:
        groups *= 5
        conditions = '?'.join([conditions] * 5)
    return conditions, groups


def count_all_arrangements(line, unfold):
    conditions, groups = parse_record(line, unfold)
    damaged_count = sum(groups)
    operational_count = len(conditions)
    splitting_operational = len(groups) - 1
    extra_operational = operational_count - damaged_count - splitting_operational
    seen_endings = {}

    def condition_matches(arrangement):
        return all(
            expected == actual
            for expected, actual in zip(conditions, arrangement)
            if expected != '?'
        )

    def count_record_arrangements(remaining_groups, extra_operational, accumulated=''):
        key = tuple(remaining_groups), extra_operational, len(accumulated)
        if key in seen_endings:
            return seen_endings[key]
        if not condition_matches(accumulated):
            return 0
        if not remaining_groups:
            return condition_matches(accumulated + '.'*extra_operational)

        total = 0
        [group, *remaining_groups] = remaining_groups
        for extra in range(extra_operational + 1):
            operational = '.'*extra
            damaged = '#'*group
            total += count_record_arrangements(
                remaining_groups,
                extra_operational - extra,
                accumulated + operational + damaged + '.'
            )
        seen_endings[key] = total
        return total

    return count_record_arrangements(groups, extra_operational)


def part_one(lines: list[str]):
    return sum(
        count_all_arrangements(line, False)
        for line in lines
    )


def part_two(lines: list[str]):
    return sum(
        count_all_arrangements(line, True)
        for line in lines
    )
