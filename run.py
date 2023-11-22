from importlib import import_module
from sys import argv


day = f'{int(argv[1]):02d}'
solver = import_module(f'{day}_solver')

lines = open(f'{day}_input.txt', 'r').read().splitlines()

print()

print(f'Day {day}: {solver.name}')

print()

part_1 = solver.part_1(lines)
part_2 = solver.part_2(lines)

print()

print('Part one:', part_1)
print('Part two:', part_2)

print()
