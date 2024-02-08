# Day 23: A Long Walk

name = 'Day 23: A Long Walk'

part_one_verified = 2250
part_two_verified = 6470

walkable = '.^v><'


def part_one(lines: list[str]):
    land = {
        (y, x): c
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if c in walkable
    }
    start, end = min(land), max(land)
    tracked_steps = [(start, set())]
    max_hike = 0
    while tracked_steps:
        current, visited = tracked_steps.pop()
        visited = set(visited)
        visited.add(current)
        if current == end:
            max_hike = max(max_hike,  len(visited))
            continue
        cy, cx = current
        adjacent = []
        if land[current] in '.>':
            adjacent.append((cy, cx+1))
        if land[current] in '.<':
            adjacent.append((cy, cx-1))
        if land[current] in '.v':
            adjacent.append((cy+1, cx))
        if land[current] in '.^':
            adjacent.append((cy-1, cx))

        adjacent = [
            adj
            for adj in adjacent
            if (adj in land)
            and (adj not in visited)
        ]

        if not adjacent:
            continue

        for adj in adjacent:
            tracked_steps.append((adj, visited))

    return max_hike - 1


def parse_network(lines):
    delta_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    network = {
        (y, x): set()
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if c in walkable
    }

    for (y, x), s in network.items():
        for dy, dx in delta_pos:
            adj = y+dy, x+dx
            if adj in network:
                s.add(adj)

    return network


def find_links(network):
    start, end = sorted(node for node in network if len(network[node]) == 1)
    nodes = {node for node in network if len(network[node]) != 2}
    links = {}
    for node in nodes:
        links[node] = []
        for current in network[node]:
            steps = 1
            seen = {node, current}
            while current not in nodes:
                current = next(x for x in network[current] if x not in seen)
                seen.add(current)
                steps += 1
            links[node].append((current, steps))
    return start, end, links


def part_two(lines: list[str]):
    network = parse_network(lines)
    start, end, links = find_links(network)
    start_node, start_distance = links[start][0]
    end_node, end_distance = links[end][0]

    def find_longest_hike(current, total_distance, visited):
        if current == end_node:
            yield total_distance
            return

        visited = visited | {current}
        for node, link_distance in links[current]:
            if node not in visited:
                yield from find_longest_hike(node, total_distance + link_distance, visited)

    ends_distance = start_distance + end_distance
    return max(find_longest_hike(start_node, ends_distance, {start, end}))
