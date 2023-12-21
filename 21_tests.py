# Day 21: Step Counter - Tests

test_input = [
    '...........',
    '.....###.#.',
    '.###.##..#.',
    '..#.#...#..',
    '....#.#....',
    '.##..S####.',
    '.##..#...#.',
    '.......##..',
    '.##.#.####.',
    '.##..##.##.',
    '...........',
]

part_one = [
    {'expected': 16, 'input': test_input, 'args': [6]},
]

part_two = [
    {'expected': 16, 'input': test_input, 'args': [6]},
    {'expected': 50, 'input': test_input, 'args': [10]},
    {'expected': 1594, 'input': test_input, 'args': [50]},
    {'expected': 6536, 'input': test_input, 'args': [100]},
    {'expected': 167004, 'input': test_input, 'args': [500]},
    {'expected': 668697, 'input': test_input, 'args': [1000]},
    {'expected': 16733044, 'input': test_input, 'args': [5000]},

]
