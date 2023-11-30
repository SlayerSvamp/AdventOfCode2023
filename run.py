from importlib import import_module
from sys import argv, stdout
from glob import glob
from clock import clock
from style import *

if len(argv) > 1:
    day = f'{int(argv[1]):02d}'
else:
    files = glob('*_solver.py')
    day = max(file[:2] for file in files)
solver = import_module(f'{day}_solver')

with open(f'{day}_input.txt', 'r') as file:
    lines = file.read().splitlines()


def run(solve):
    print(f'{solve.__name__}{fg.gray}... ', end='')
    stdout.flush()
    [answer, time_one] = clock(solve, lines)
    print(f'done! - {reset}{time_one}')
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

part_one = run(solver.part_one)
part_two = run(solver.part_two)


def get_color(expected, actual):
    if expected == None:
        return fg.blue
    if str(expected) == str(actual):
        return fg.yellow
    return fg.red


part_one_color = get_color(solver.part_one_verified, part_one)
part_two_color = get_color(solver.part_two_verified, part_two)

print(f"""

{fg.gray}Results:{reset}
{divider.single}
{fg.gray}Part{reset} one: {em.bold}{part_one_color}{part_one}{reset}
{fg.gray}Part{reset} two: {em.bold}{part_two_color}{part_two}{reset}


{fg.green}{em.bold}Done!{reset}

{divider.spiral}
""")
