# Day 20: Pulse Propagation

name = 'Day 20: Pulse Propagation'

part_one_verified = 919383692
part_two_verified = 247702167614647


def parse_module_list(lines):
    for line in lines:
        identifier, destinations = line.split(' -> ')
        module_name = module_type = identifier
        if identifier != 'broadcaster':
            module_type = identifier[0]
            module_name = identifier[1:]
        yield module_name, module_type, destinations.split(', ')


def get_all_conjunctions(module_lookup):
    conjunction = {}
    for name, (_, destinations) in module_lookup.items():
        for destination in destinations:
            if destination in module_lookup and module_lookup[destination][0] == '&':
                conjunction.setdefault(destination, {})
                conjunction[destination][name] = 0
    return conjunction


def press_button(module_lookup, flip_flop, conjunction):
    low_pulses = 0
    high_pulses = 0
    pulses = [('button', 0, 'broadcaster')]
    while pulses:
        next_pulses = []
        for source, pulse, module_name in pulses:
            if pulse:
                high_pulses += 1
            else:
                low_pulses += 1
            if module_name not in module_lookup:
                continue
            module_type, destinations = module_lookup[module_name]
            if module_type == 'broadcaster':
                next_pulse = pulse
            if module_type == '%':
                if pulse:
                    continue
                flip_flop[module_name] ^= 1
                next_pulse = flip_flop[module_name]
            if module_type == '&':
                conjunction[module_name][source] = pulse
                next_pulse = int(not all(conjunction[module_name].values()))
            for destination in destinations:
                next_pulses.append((module_name, next_pulse, destination))
        pulses = next_pulses
    return low_pulses, high_pulses


def parse_module_connections(lines):
    module_lookup = {n: (t, d) for n, t, d in parse_module_list(lines)}
    flip_flop = {n: 0 for n, (t, _) in module_lookup.items() if t == '%'}
    conjunction = get_all_conjunctions(module_lookup)
    return module_lookup, flip_flop, conjunction


def get_source_modules(module_lookup, target):
    for module, (_, destinations) in module_lookup.items():
        for destination in destinations:
            if destination == target:
                yield module


def find_module_dependency_arrays(module_lookup):
    destinations = ['rx']
    while destinations:
        new_targets = []
        for target in destinations:
            sources = tuple(get_source_modules(module_lookup, target))
            if any(module_lookup[source][0] == '%' for source in sources):
                yield sources
            else:
                new_targets.extend(sources)
        destinations = new_targets


def find_module_switch_count(module_lookup, flip_flop, conjunction):
    modules = {module for module, (t, _) in module_lookup.items() if t == '%'}
    module_switch_count = {}
    press_count = 0
    while modules:
        press_count += 1
        press_button(module_lookup, flip_flop, conjunction)
        for module in set(modules):
            if flip_flop[module]:
                module_switch_count[module] = press_count
                modules.remove(module)
    return module_switch_count


def part_one(lines: list[str]):
    module_lookup, flip_flop, conjunction = parse_module_connections(lines)
    total_low_pulses = 0
    total_high_pulses = 0
    for _ in range(1000):
        low_pulses, high_pulses = press_button(
            module_lookup, flip_flop, conjunction)
        total_low_pulses += low_pulses
        total_high_pulses += high_pulses
    return total_low_pulses * total_high_pulses


def part_two(lines: list[str]):
    """
    cs -> qb -> dr -> rx
    dx -> mp -> dr -> rx
    ck -> qt -> dr -> rx
    jh -> ng -> dr -> rx

    those are my personal data dependency sources for conjunction modules
    every "root" conjunction module has its own dependencies in a handful of flip flops
    combined to a sum of the frequency in flipping between low and high, they produce prime numbers
    multiplying those prime numbers together produces the answer to how many times you have to press the button

    note:
    for some reason i cant seem to find any state after a completed button press where the root conjunctions are 
    in the correct state, so i have to depend on the root conjunctions own flip flop states
    """
    module_lookup, flip_flop, conjunction = parse_module_connections(lines)
    module_bit_order = find_module_switch_count(
        module_lookup, flip_flop, conjunction)
    target_button_press_count = 1
    for module_dependencies in find_module_dependency_arrays(module_lookup):
        dependency_frequency = sum(
            module_bit_order[module]
            for module in module_dependencies
        )
        target_button_press_count *= dependency_frequency
    return target_button_press_count
