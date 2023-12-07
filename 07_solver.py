# Day 7: Camel Cards

import re


name = 'Day 7: Camel Cards'

part_one_verified = 250232501
part_two_verified = 249138943

values = 'j123456789TJQKA'


def get_hand_type(cards):
    cards = ''.join(sorted(cards, key=values.index))
    expression_types = [
        (r'(.)\1{4}', 5),
        (r'(.)\1{3}', 4),
        (r'(.)\1\1(.)\2|(.)\3(.)\4\4', 3.5),
        (r'(.)\1\1', 3),
        (r'(.)\1.?(.)\2', 2.5),
        (r'(.)\1', 2),
    ]
    for exp, hand_type in expression_types:
        if re.search(exp, cards):
            return hand_type
    return 1


def parse_hand(line: str):
    cards, bid = line.split(' ')
    hand_type = (
        get_hand_type(c for c in cards if c != 'j')
        + min(4, cards.count('j'))
    )
    tiebreaker = list(map(values.index, cards))
    return (hand_type, tiebreaker), int(bid)


def part_one(lines: list[str]):
    hands = sorted(parse_hand(x) for x in lines)
    ranked = [(i+1, bid) for i, (_, bid) in enumerate(hands)]
    return sum(rank * bid for rank, bid in ranked)


def part_two(lines: list[str]):
    return part_one([
        line.replace('J', 'j')
        for line in lines
    ])
