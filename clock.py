from time import time_ns
from style import *


def clock(solve, lines, args=[]) -> list[any, str]:
    start = time_ns()
    answer = solve(lines, *args)
    end = time_ns()
    time = f'{(end - start)/10**9:.2f} {fg.gray}seconds{reset}'
    return [answer, time]
