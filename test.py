from importlib import import_module
from sys import argv
from glob import glob
from style import *

if len(argv) > 1:
    day = f'{int(argv[1]):02d}'
else:
    files = glob('*_solver.py')
    day = max(file[:2] for file in files)
solver = import_module(f'{day}_solver')
tests = import_module(f'{day}_tests')


print(f"""
{divider.spiral}{em.dim}

 ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
 ╚═╗ ╔═╝ ║ ╔═══╝ ║ ╔═══╝ ╚═╗ ╔═╝
   ║ ║   ║ ╚══╗  ║ ╚═══╗   ║ ║
   ║ ║   ║ ╔══╝  ╚═══╗ ║   ║ ║
   ║ ║   ║ ╚═══╗ ╔═══╝ ║   ║ ║
   ╚═╝   ╚═════╝ ╚═════╝   ╚═╝
   {reset}{solver.name}
""")

parts = [
    (tests.part_one, solver.part_one),
    (tests.part_two, solver.part_two),
]
for cases, run in parts:
    print()
    print(f'{em.dim}Testing {run.__name__}:{reset}')
    print(divider.single)
    for i, case in enumerate(cases):
        print(
            f'case {i + 1}{em.dim}/{reset}{len(cases)}{em.dim}...{reset} ', end='')
        expected = case.get('expected')
        inp = case.get('input')
        actual = str(run(inp))
        if actual == expected:
            print(f'{fg.green}done!{reset}')
        else:
            print(f'{fg.red}fail!{reset}')
            print(f'{em.dim} expected: "{reset}' +
                  f'{fg.blue}{expected}{reset}{em.dim}"{reset}')
            print(f'{em.dim}   actual: "{reset}' +
                  f'{fg.blue}{actual}{reset}{em.dim}"{reset}')
    print()

print(f"""
{fg.green}{em.bold}All tests done!{reset}

{divider.spiral}
""")
