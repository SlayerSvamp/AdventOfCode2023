# Day 19: Aplenty

name = 'Day 19: Aplenty'

part_one_verified = 434147
part_two_verified = 136146366355609


def parse_workflows(lines):
    def pairs():
        end = lines.index('')
        for line in lines[:end]:
            name, rules = line[:-1].split('{')
            yield name, rules.split(',')
    return dict(pairs())


def parse_parts(lines):
    start = lines.index('') + 1
    for line in lines[start:]:
        part = {}
        for pair in line[1:-1].split(','):
            category, rating = pair.split('=')
            part[category] = int(rating)
        yield part


def parse_rule(rule):
    [category, _, *rating], key = rule.split(':')
    return key, category, int(''.join(rating))


def part_is_accepted(workflows, part):
    def test_key(key):
        if key in 'RA':
            return key == 'A'
        for rule in workflows[key]:
            if rule in 'RA' or rule in workflows:
                return test_key(rule)
            next_key, category, rating = parse_rule(rule)
            if '<' in rule and part[category] < rating:
                return test_key(next_key)
            if '>' in rule and part[category] > rating:
                return test_key(next_key)
    return test_key('in')


def count_accepted_combinations(workflows):
    def inner(ratings, key):
        if key == 'R':
            return 0
        if key == 'A':
            combinations = 1
            for min_rating, max_rating in ratings.values():
                combinations *= max_rating - min_rating + 1
            return combinations
        acceptable_combinations = 0
        for rule in workflows[key]:
            next_ratings = dict(ratings)
            next_key = rule
            if ':' in rule:
                next_key, category, rating = parse_rule(rule)
                min_rating, max_rating = ratings[category]
                if '<' in rule:
                    next_ratings[category] = (min_rating, rating - 1)
                    ratings[category] = (rating, max_rating)
                elif '>' in rule:
                    next_ratings[category] = (rating + 1, max_rating)
                    ratings[category] = (min_rating, rating)
            acceptable_combinations += inner(next_ratings, next_key)
        return acceptable_combinations

    all_ratings = {category: (1, 4000) for category in 'xmas'}
    return inner(all_ratings, 'in')


def part_one(lines: list[str]):
    workflows = parse_workflows(lines)
    parts = parse_parts(lines)
    return sum(
        sum(part.values())
        for part in parts
        if part_is_accepted(workflows, part)
    )


def part_two(lines: list[str]):
    workflows = parse_workflows(lines)
    return count_accepted_combinations(workflows)
