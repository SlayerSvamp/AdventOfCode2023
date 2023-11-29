from importlib import import_module
from sys import argv
from glob import glob
from time import time_ns
from style import *

if len(argv) > 1:
    day = f'{int(argv[1]):02d}'
else:
    files = glob('*_solver.py')
    day = max(file[:2] for file in files)
solver = import_module(f'{day}_solver')

lines = open(f'{day}_input.txt', 'r').read().splitlines()


def clock(solve) -> str:
    print(f'{solve.__name__}{fg.gray}... ', end='')
    start = time_ns()
    answer = solve(lines)
    end = time_ns()
    print('done in', end=reset)
    print(f'{(end - start)/10**9: .2f} {fg.gray}seconds{reset}')
    return answer


print(f"""
{divider.spiral}{fg.gray}

 ╔═══════╗ ╔═╗   ╔═╗ ╔═══════╗
 ║ ╔═══╗ ║ ║ ║   ║ ║ ║ ╔═══╗ ║
 ║ ╚═══╝ ║ ║ ║   ║ ║ ║ ║   ║ ║
 ║ ╔═╗ ╔═╝ ║ ║   ║ ║ ║ ║   ║ ║
 ║ ║ ║ ╚═╗ ║ ╚═══╝ ║ ║ ║   ║ ╚═╗
 ╚═╝ ╚═══╝ ╚═══════╝ ╚═╝   ╚═══╝
 {reset}{solver.name}


{fg.gray}Running:{reset}
{divider.single}
""".rstrip())

part_one = clock(solver.part_one)
part_two = clock(solver.part_two)

print(f"""

{fg.gray}Results:{reset}
{divider.single}
{fg.gray}Part{reset} one: {em.bold}{fg.bright.yellow}{part_one}{reset}
{fg.gray}Part{reset} two: {em.bold}{fg.bright.yellow}{part_two}{reset}


{fg.green}{em.bold}Done!{reset}

{divider.spiral}
""")
