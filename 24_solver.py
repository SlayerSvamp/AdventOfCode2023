# Day 24: Never Tell Me The Odds

name = 'Day 24: Never Tell Me The Odds'

part_one_verified = None
part_two_verified = None


def parse_hailstones(lines):
    return [
        [int(x) for x in line.replace(r' @ ', ', ').split(', ')]
        for line in lines
    ]


def sign(v):
    return v / abs(v) if v else 0


def intersects(hs1, hs2):
    px1, py1, pz1, vx1, vy1, vz1 = hs1
    px2, py2, pz2, vx2, vy2, vz2 = hs2
    dpx = px2 - px1
    dvx = vx1 - vx2
    dpy = py2 - py1
    dvy = vy1 - vy2

    if sign(dpx) != sign(dvx):
        return False
    if sign(dpy) != sign(dvy):
        return False
    return True


def part_one(lines: list[str], limits=[200000000000000, 400000000000000]):
    lim_min, lim_max = limits
    hailstones = list(parse_hailstones(lines))
    pairs = [
        (hs1, hs2)
        for i, hs1 in enumerate(hailstones)
        for hs2 in hailstones[i+1:]
        if intersects(hs1, hs2)
    ]

    res = len(pairs)
    if limits[0] > 10000:
        assert res > 4260, res
    return res


def part_two(lines: list[str]):
    pass
