# Day 6: Wait For It

from functools import reduce
from re import split as re_split


name = 'Day 6: Wait For It'

part_one_verified = 1710720
part_two_verified = 35349468


def get_ways(pair):
    time, distance = pair
    ways = 0
    for t in range(time):
        if t * (time - t) > distance:
            ways += 1
    return ways


def part_one(lines: list[str]):
    times = list(map(int, re_split(r' +', lines[0])[1:]))
    distances = list(map(int, re_split(r' +', lines[1])[1:]))
    races = list(map(get_ways, zip(times, distances)))
    return reduce(lambda a, b: a*b, races)


def part_two(lines: list[str]):
    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    return get_ways((time, distance))
