# Day 8: Haunted Wasteland

from math import lcm


name = 'Day 8: Haunted Wasteland'

part_one_verified = 20659
part_two_verified = 15690466351717


def parse_documents(lines):
    instructions = lines[0]
    network = {n[:3]: (n[7:10], n[12:15]) for n in lines[2:]}
    return instructions, network


def count_steps(node, instructions, network):
    steps = 0
    while not node.endswith('Z'):
        pos = steps % len(instructions)
        instruction = instructions[pos]
        node = network[node]['LR'.index(instruction)]
        steps += 1
    return steps


def part_one(lines: list[str]):
    instructions, network = parse_documents(lines)
    return count_steps('AAA', instructions, network)


def part_two(lines: list[str]):
    instructions, network = parse_documents(lines)
    return lcm(*[
        count_steps(node, instructions, network)
        for node in network
        if node.endswith('A')
    ])
