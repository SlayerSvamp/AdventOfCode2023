# Day 15: Lens Library

name = 'Day 15: Lens Library'

part_one_verified = 517315
part_two_verified = 247763


def hash_algorithm(string):
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def part_one(lines: list[str]):
    strings = lines[0].split(',')
    return sum(hash_algorithm(string) for string in strings)


def part_two(lines: list[str]):
    steps = lines[0].split(',')
    boxes = [[] for _ in range(256)]
    for step in steps:
        split_index = step.index('=') if '=' in step else step.index('-')
        lens_name = step[:split_index]
        box = boxes[hash_algorithm(lens_name)]
        op = step[split_index:]
        if op.startswith('='):
            for slot_index, lens in enumerate(box):
                if lens.startswith(lens_name):
                    box[slot_index] = step
                    break
            else:
                box.append(step)
        elif op == '-':
            for slot_index, lens in enumerate(box):
                if lens.startswith(lens_name):
                    box.pop(slot_index)

    total = 0
    for box_index, box in enumerate(boxes):
        for slot_index, lens_name in enumerate(box):
            focal_length = int(lens_name.split('=')[1])
            total += (box_index + 1) * (slot_index + 1) * focal_length
    return total
