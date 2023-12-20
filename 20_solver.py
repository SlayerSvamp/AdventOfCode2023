# Day 20: Pulse Propagation

name = 'Day 20: Pulse Propagation'

part_one_verified = None
part_two_verified = None


def parse_module_list(lines):
    for line in lines:
        identifier, destinations = line.split(' -> ')
        module_name = module_type = identifier
        if identifier != 'broadcaster':
            module_type = identifier[0]
            module_name = identifier[1:]
        yield module_name, module_type, destinations.split(', ')


def get_all_conjunctions(modules):
    conjunction = {}
    conjunction['button'] = {'broadcaster': 0}
    for name, (_, destinations) in modules.items():
        for destination in destinations:
            if destination in modules and modules[destination][0] == '&':
                conjunction.setdefault(destination, {})
                conjunction[destination][name] = 0
    return conjunction


def part_one(lines: list[str]):
    modules = {n: (t, d) for n, t, d in parse_module_list(lines)}
    low_pulses = 0
    high_pulses = 0
    flip_flop = {n: 0 for n, (t, _) in modules.items() if t == '%'}
    conjunction = get_all_conjunctions(modules)
    for press_i in range(1000):
        pulses = [('button', 0, 'broadcaster')]
        while pulses:
            next_pulses = []
            for source, pulse, module_name in pulses:
                if not press_i:
                    print(f'{source} -{pulse}-> {module_name}')
                    input()
                if pulse:
                    high_pulses += 1
                else:
                    low_pulses += 1
                if module_name not in modules:
                    continue
                module_type, destinations = modules[module_name]
                if module_type == 'broadcaster':
                    next_pulse = pulse
                if module_type == '%':
                    if pulse:
                        continue
                    flip_flop[module_name] ^= 1
                    next_pulse = flip_flop[module_name]
                if module_type == '&':
                    conjunction[module_name][source] = next_pulse
                    next_pulse = int(
                        not all(conjunction[module_name].values()))

                for destination in destinations:
                    next_pulses.append((module_name, next_pulse, destination))
            pulses = next_pulses

    print()
    print(low_pulses, high_pulses)
    return low_pulses * high_pulses


def part_two(lines: list[str]):
    pass
