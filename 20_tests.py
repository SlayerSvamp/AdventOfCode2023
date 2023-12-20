# Day 20: Pulse Propagation - Tests

part_one = [
    {'expected': 32000000, 'input': [
        'broadcaster -> a, b, c',
        '%a -> b',
        '%b -> c',
        '%c -> inv',
        '&inv -> a',
    ]},
    {'expected': 11687500, 'input': [
        'broadcaster -> a',
        '%a -> inv, con',
        '&inv -> b',
        '%b -> con',
        '&con -> output',
    ]},
]

part_two = [
    {'expected': '', 'input': ['']},
]
