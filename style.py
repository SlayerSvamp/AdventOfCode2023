reset = '\033[0m'


class em:
    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    strike = '\033[9m'


class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    default = '\033[39m'

    class bright:
        black = '\033[90m'
        red = '\033[91m'
        green = '\033[92m'
        yellow = '\033[93m'
        blue = '\033[94m'
        magenta = '\033[95m'
        cyan = '\033[96m'
        white = '\033[97m'
        default = '\033[99m'


class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'
    default = '\033[49m'

    class bright:
        black = '\033[100m'
        red = '\033[101m'
        green = '\033[102m'
        yellow = '\033[103m'
        blue = '\033[104m'
        magenta = '\033[105m'
        cyan = '\033[106m'
        white = '\033[107m'
        default = '\033[109m'


class divider:
    single = em.dim + '-'*33 + reset
    double = em.dim + '='*33 + reset
    spiral = em.dim + '%'*33 + reset
