# Day 19: Aplenty

import re


name = 'Day 19: Aplenty'

part_one_verified = 434147
part_two_verified = None


def parse_workflows(lines):
    workflows = {}
    for line in lines:
        name, rules = line[:-1].split('{')
        workflows[name] = rules.split(',')
    return workflows


def parse_parts(lines):
    return [
        {
            k: int(v) for k, v
            in [raw.split('=') for raw in line[1:-1].split(',')]}
        for line in lines
    ]


def process_part(workflows, part):
    workflow = 'in'
    while workflow in workflows:
        for rule in workflows[workflow]:
            if rule in 'RA':
                return rule
            if rule in workflows:
                workflow = rule
                break
            if '<' in rule:
                key, value, next_workflow = re.split(r'[<:]', rule)
                if part[key] < int(value):
                    workflow = next_workflow
                    break
            elif '>' in rule:
                key, value, next_workflow = re.split(r'[>:]', rule)
                if part[key] > int(value):
                    workflow = next_workflow
                    break
    return workflow


def part_one(lines: list[str]):
    i = lines.index('')
    workflows = parse_workflows(lines[:i])
    parts = parse_parts(lines[i+1:])
    return sum(sum(part.values()) for part in parts if process_part(workflows, part) == 'A')


def part_two(lines: list[str]):
    pass
