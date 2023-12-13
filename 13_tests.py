# Day 13: Point of Incidence - Tests

test_input_1 = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
]

test_input_2 = [
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#',
]

part_one = [
    {'expected': 5, 'input': test_input_1},
    {'expected': 400, 'input': test_input_2},
    {'expected': 405, 'input': test_input_1 + [''] + test_input_2},

]

part_two = [
    {'expected': 300, 'input': test_input_1},
    {'expected': 100, 'input': test_input_2},
    {'expected': 400, 'input': test_input_1 + [''] + test_input_2},
]
