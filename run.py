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
    print(f'{solve.__name__}{em.dim}... ', end='')
    start = time_ns()
    answer = solve(lines)
    end = time_ns()
    print('done in', end=reset)
    print(f'{(end - start)/10**9: .2f} {em.dim}seconds{reset}')
    return answer


print(f"""
{divider.spiral}{em.dim}

 ╔═══════╗ ╔═╗   ╔═╗ ╔═══════╗
 ║ ╔═══╗ ║ ║ ║   ║ ║ ║ ╔═══╗ ║
 ║ ╚═══╝ ║ ║ ║   ║ ║ ║ ║   ║ ║
 ║ ╔═╗ ╔═╝ ║ ║   ║ ║ ║ ║   ║ ║
 ║ ║ ║ ╚═╗ ║ ╚═══╝ ║ ║ ║   ║ ╚═╗
 ╚═╝ ╚═══╝ ╚═══════╝ ╚═╝   ╚═══╝
 {reset}{solver.name}


{em.dim}Running:{reset}
{divider.single}
""".rstrip())

part_one = clock(solver.part_one)
part_two = clock(solver.part_two)

print(f"""

{em.dim}Results:{reset}
{divider.single}
{em.dim}Part{reset} one: {em.bold}{fg.bright.yellow}{part_one}{reset}
{em.dim}Part{reset} two: {em.bold}{fg.bright.yellow}{part_two}{reset}


{fg.green}{em.bold}Done!{reset}

{divider.spiral}
""")
