# Day 1: Trebuchet?!

name = 'Day 1: Trebuchet?!'

part_one_verified = 55834
part_two_verified = 53221


def part_one(lines: list[str]):
    total = 0
    for line in lines:
        nums = [*filter(str.isnumeric, line)]
        total += int(nums[0] + nums[-1])
    return total


def part_two(lines: list[str]):
    numbers = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    total = 0
    for line in lines:
        number_indices = [
            (i, str(numbers.index(n)))
            for i in range(len(line))
            for n in numbers if line[i:].startswith(n)
        ]
        digits = [(i, c) for i, c in enumerate(line) if c.isnumeric()]
        nums = [x[1] for x in sorted(number_indices + digits)]
        total += int(nums[0] + nums[-1])
    return total
