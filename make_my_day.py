# Make my day

from style import divider


def prompt(text):
    return input(text + '\n')


print(f"""
{divider.spiral}

Time to make my day!
What day of december is it?
""".rstrip())
inp = input()
day = f'{int(inp):02d}'

print(f"""
What is the name of today's puzzle?
""".rstrip())
name = input()
full_name = f'Day {int(day)}: {name}'

open(f'{day}_input.txt', 'a')
test_json = open(f'{day}_tests.py', 'a')
test_json.write(f"""

# {full_name} - Tests

part_one = [
    {{'expected': '', 'input': ['']}},
]

part_two = [
    {{'expected': '', 'input': ['']}},
]

""".strip() + '\n')

py = open(f'{day}_solver.py', 'a')
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
