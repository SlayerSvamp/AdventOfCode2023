# Make my day

def prompt(text):
    return input(text + '\n')


print()

print('Time to make my day!')

print()

print('What day of december is it?')
inp = input()
day = f'{int(inp):02d}'

print()

print("What is the name of today's puzzle?")
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


def part_one(lines: list[str]):
    pass


def part_two(lines: list[str]):
    pass

""".strip() + '\n')
py.close()
