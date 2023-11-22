# Make my day

def prompt(text):
    return input(text + '\n')


def confirm(text):
    s = prompt(text + ' (Y/n)')
    return s in ('Y', 'y', '')


print()

print('Time to make my day!')

print()

day = prompt('What day of december is it?')

if len(day) < 2:
    day = f'0{day}'

print()

name = prompt("What is the name of today's puzzle?")

open(f'{day}_input.txt', 'a')
test_json = open(f'{day}_tests.py', 'a')
test_json.write("""

# tests for day {day}: {name}

part_1 = [
    {'expected': '', 'input':  ['']},
]

part_2 = [
    {'expected': '', 'input':  ['']},
]

""".strip() + '\n')

py = open(f'{day}_solver.py', 'a')
py.write(f"""

# {name}

from common import timer

name = '{name}'


@timer
def part_1(lines: list[str]):
    pass


@timer
def part_2(lines: list[str]):
    pass

""".strip() + '\n')
py.close()
