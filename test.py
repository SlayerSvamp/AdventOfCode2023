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
tests = import_module(f'{day}_tests')


print(f"""
{divider.spiral}{fg.gray}

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
    print(f'{fg.gray}Testing {run.__name__}:{reset}')
    print(divider.single)
    for i, case in enumerate(cases):
        def gray(x): return f'{fg.gray}{x}{reset}'
        print(f'case {i + 1}{gray("/")}{len(cases)}{gray("...")} ', end='')
        stdout.flush()
        expected = case.get('expected')
        inp = case.get('input')
        [result, time] = clock(run, inp)
        actual = str(result)
        if actual == expected:
            print(f'{fg.green}done!{reset}{fg.gray} - {reset}{time}')
        else:
            print(f'{fg.red}fail!{reset}{fg.gray} - {reset}{time}')
            print(f'{fg.gray} expected: "{reset}' +
                  f'{fg.blue}{expected}{reset}{fg.gray}"{reset}')
            print(f'{fg.gray}   actual: "{reset}' +
                  f'{fg.blue}{actual}{reset}{fg.gray}"{reset}')
    print()

print(f"""
{fg.green}{em.bold}All tests done!{reset}

{divider.spiral}
""")
