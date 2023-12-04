# Day 4: Scratchcards

name = 'Day 4: Scratchcards'

part_one_verified = 25651
part_two_verified = 19499881


def parse_cards(lines):
    for line in lines:
        _, data = line.split(':')
        [left, right] = data.split('|')
        winning_numbers = {int(x) for x in left.split(' ') if x}
        my_numbers = {int(x) for x in right.split(' ') if x}
        yield len(winning_numbers & my_numbers)


def part_one(lines: list[str]):
    points = 0
    for matching in parse_cards(lines):
        if matching:
            points += 1 << matching - 1
    return points


def part_two(lines: list[str]):
    cards = [1] * len(lines)
    total_cards = 0
    for matching in parse_cards(lines):
        n_cards = cards.pop(0)
        total_cards += n_cards
        for i in range(matching):
            cards[i] += n_cards
    return total_cards
