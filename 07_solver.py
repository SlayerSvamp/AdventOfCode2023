# Day 7: Camel Cards

import re


name = 'Day 7: Camel Cards'

part_one_verified = 250232501
part_two_verified = None

values = '0123456789TJQKA'


def get_rank_base(cards):
    scards = ''.join(sorted(cards, key=values.index))
    # five of a kind
    if re.search(r'(.)\1{4}', scards):
        return 5
    # four of a kind
    if re.search(r'(.)\1{3}', scards):
        return 4
    # full house
    if re.search(r'(.)\1\1(.)\2', scards) or re.search(r'(.)\1(.)\2\2', scards):
        return 3.5
    # three of a kind
    if re.search(r'(.)\1\1', scards):
        return 3
    # two pairs
    if re.search(r'(.)\1.?(.)\2', scards):
        return 2
    # one pair
    if re.search(r'(.)\1', scards):
        return 1
    # high card
    return 0


def parse_hand(line):
    cards, bid = line.split(' ')
    utslag = list(map(values.index, cards))
    return (get_rank_base(cards), utslag), int(bid)


def part_one(lines: list[str]):
    hands = sorted(parse_hand(line) for line in lines)
    ranked = [(i+1, bid) for i, (_, bid) in enumerate(hands)]
    return sum(rank*bid for rank, bid in ranked)


def part_two(lines: list[str]):
    pass
