# Day 6: Wait For It

from math import ceil, prod

name = 'Day 6: Wait For It'

part_one_verified = 1710720
part_two_verified = 35349468


def count_ways(pair):
    time, distance = map(int, pair)
    current = 0
    step = time
    while step > 1:
        step = ceil(step / 2)
        too_high, high_enough = (
            time * i - i ** 2 > distance
            for i in [current, current + 1]
        )
        if too_high:
            current -= step
        elif not high_enough:
            current += step
    return time - current * 2 - 1


def parse_numbers(lines):
    return [
        filter(str.isnumeric, line.split(' '))
        for line in lines
    ]


def part_one(lines: list[str]):
    pairs = zip(*parse_numbers(lines))
    ways = map(count_ways, pairs)
    return prod(ways)


def part_two(lines: list[str]):
    pair = map(''.join, parse_numbers(lines))
    return count_ways(pair)
