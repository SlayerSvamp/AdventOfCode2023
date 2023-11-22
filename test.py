from importlib import import_module
from sys import argv

day = f'{int(argv[1]):02d}'
solver = import_module(f'{day}_solver')
tests = import_module(f'{day}_tests')

print()

print(f'Running tests for day {day}: {solver.name}')

print()

parts = [
    ('part 1', tests.part_1, solver.part_1),
    ('part 2', tests.part_2, solver.part_2),
]
for name, cases, run in parts:
    for case in cases:
        print(f'Testing {name}')
        expected = case.get('expected')
        inp = case.get('input')
        actual = str(run(inp))
        assert actual == expected, f'expected "{expected}", got "{actual}"'

print()

print("All tests done!")

print()
