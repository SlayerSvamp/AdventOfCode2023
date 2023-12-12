# Day 12: Hot Springs

from itertools import zip_longest


name = 'Day 12: Hot Springs'

part_one_verified = 7163
part_two_verified = None


def arrangements(nono: str, numbers: list[int]):
    if '?' not in nono:
        splitted = list(filter(bool, map(len, nono.split('.'))))
        yield all(x == y for x, y in zip_longest(numbers, splitted))
    else:
        for s in '#.':
            x = nono.replace('?', s, 1)
            yield from arrangements(x, numbers)


def part_one(lines: list[str]):

    # [expected in ('?', actual) for expected,actual in zip(nono, alt)]

    total_arrangements = 0
    for line in lines:
        nono, numbers = line.split(' ')
        numbers = list(map(int, numbers.split(',')))
        total_arrangements += sum(arrangements(nono, numbers))

    return total_arrangements


def part_two(lines: list[str]):
    return False
    total_arrangements = 0
    for line in lines:
        nono, numbers = line.split(' ')
        numbers = list(map(int, numbers.split(',')))
        nono = nono*5
        numbers = numbers*5
        total_arrangements += sum(arrangements(nono, numbers))

    return total_arrangements
