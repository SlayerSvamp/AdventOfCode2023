from sys import argv


def read_lines(day: str) -> str:
    file = f'{day}'
    if len(argv) > 1:
        file += '.' + argv[1]
    return open(f'input/{file}.txt', 'r').read().splitlines()
