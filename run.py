from importlib import import_module
from sys import argv
from time import time_ns

day = f'{int(argv[1]):02d}'
solver = import_module(f'{day}_solver')

lines = open(f'{day}_input.txt', 'r').read().splitlines()


def clock(solve) -> str:
    start = time_ns()
    answer = solve(lines)
    end = time_ns()
    print(f'{solve.__name__} ran in {(end - start)/10**9:.2f} seconds')
    return answer


print()

print(f'Day {day}: {solver.name}')

print()

part_one = clock(solver.part_one)
part_two = clock(solver.part_two)

print()

print('Part one:', part_one)
print('Part two:', part_two)

print()
