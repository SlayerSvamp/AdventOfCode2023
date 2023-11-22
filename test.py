from importlib import import_module
from sys import argv

day = f'{int(argv[1]):02d}'
solver = import_module(f'{day}_solver')
tests = import_module(f'{day}_tests')

print()

print(f'Running tests for day {day}: {solver.name}')

print()

parts = [
    (tests.part_one, solver.part_one),
    (tests.part_two, solver.part_two),
]
for cases, run in parts:
    print(f'Testing {run.__name__}:')
    for i, case in enumerate(cases):
        print(f'case {i + 1}/{len(cases)}...', end='')
        expected = case.get('expected')
        inp = case.get('input')
        actual = str(run(inp))
        assert actual == expected, f'expected "{expected}", got "{actual}"'
        print(' done!')
    print()

print("All tests done!")

print()
