# Generate day

from os import path, makedirs


def prompt(text):
    return input(text + '\n')


def confirm(text):
    s = prompt(text + ' (Y/n)')
    return s in ('Y', 'y', '')


print('Generate day')

day = prompt('What day of december is it?')

if len(day) < 2:
    day = f'0{day}'

name = prompt('What is the name of today\'s puzzle?')

input_files = confirm('Does this puzzle need a input file?')

correct = confirm(
    '\n'.join([
        f'day: {day}',
        f'name: {name}',
        f'needs input: {"yes" if input_files else "no"}',
        'Is this correct?',
    ])
)

if correct:
    py = open(f'{day}.py', 'a')
    if input_files:
        if not path.exists('input'):
            makedirs('input')

        open(f'input/{day}.txt', 'a')
        open(f'input/{day}.test.txt', 'a')

    py_lines = [f"""
# {name}

from read_input import read_lines
from timer import timer

""".strip()]

    if input_files:
        py_lines.append(f"""

lines = read_lines('{day}')
""")

    py_lines.append(f"""

@timer
def run_part_1():
    pass


@timer
def run_part_2():
    pass


print()

print('Day {day}: {name}')

print()

part_1 = run_part_1()
part_2 = run_part_2()

print()

print('Part one:', part_1)
print('Part two:', part_2)

print()
""")

    py.writelines(py_lines)

else:
    print('no? oh well...\ngoodbye!')
