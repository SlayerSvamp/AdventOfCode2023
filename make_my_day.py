# Make my day

from style import *


def prompt(text):
    return input(text + '\n')


print(f"""
{divider.spiral}{fg.gray}

  ╔════╗╔═╗ ╔═════╗ ╔═╗    ╔═╗
  ║ ╔═╗║║ ║ ║ ╔═══╝ ║ ║    ║ ║
  ║ ║ ║║║ ║ ║ ╚══╗  ║ ║╔══╗║ ║
  ║ ║ ║║║ ║ ║ ╔══╝  ║ ║║╔╗║║ ║
  ║ ║ ║╚╝ ║ ║ ╚═══╗ ║ ╚╝║║╚╝ ║
  ╚═╝ ╚═══╝ ╚═════╝ ╚═══╝╚═══╝
  {reset}Time to make my day!

{fg.gray}Collection info:{reset}
{divider.single}
What day of december is it?
""".rstrip())
inp = input()
day = f'{int(inp):02d}'

print(f"""
What is the name of today's puzzle?
""".rstrip())
name = input()
full_name = f'Day {int(day)}: {name}'

print(f'''
{fg.gray}Creating files:{reset}
{divider.single}
'''.rstrip())

input_filename = f'{day}_input.txt'
print(input_filename)
open(input_filename, 'a')

test_filename = f'{day}_tests.py'
print(test_filename)
test_py = open(test_filename, 'a')
test_py.write(f"""

# {full_name} - Tests

part_one = [
    {{'expected': '', 'input': ['']}},
]

part_two = [
    {{'expected': '', 'input': ['']}},
]

""".strip() + '\n')

solver_filename = f'{day}_solver.py'
print(solver_filename)
py = open(solver_filename, 'a')
py.write(f"""

# {full_name}

name = '{full_name}'

part_one_verified = None
part_two_verified = None


def part_one(lines: list[str]):
    pass


def part_two(lines: list[str]):
    pass

""".strip() + '\n')
py.close()

print(f'''
{fg.gray}Created{reset} {fg.blue}{full_name}{reset}

{fg.green}Done!{reset}

{divider.spiral}
''')
