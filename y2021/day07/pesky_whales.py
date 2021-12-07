from y2021.helpers import read


def least_fuel_required(crab_posns):
    # pt1
    posn_fuel = {}
    for posn in range(0, max(crab_posns) + 1):
        # in theory the position could be outside this range but let's gamble that it's not
        fuel_rqd = sum([max(c, posn) - min(c, posn) for c in crab_posns])
        posn_fuel[posn] = fuel_rqd
    return min(posn_fuel.values())


# pt2
def how_much_fuel(from_pos, to_pos):
    burn_rate = 1
    fuel_consumed = 0
    step = -1 if to_pos < from_pos else 1
    for posn in range(from_pos, to_pos, step):
        # print(f"{posn=}, before {burn_rate=}, {fuel_consumed=}")
        fuel_consumed += burn_rate
        burn_rate += 1
    return fuel_consumed


def least_fuel_required_increase_burn_rate(crab_posns):
    # this could be a lot faster but it worked so :shipitparrot:
    posn_fuel = {}
    for posn in range(0, max(crab_posns) + 1):
        # in theory the position could be outside this range but let's gamble that it's not
        fuel_rqd = sum([how_much_fuel(from_pos=c, to_pos=posn) for c in crab_posns])
        posn_fuel[posn] = fuel_rqd
    return min(posn_fuel.values())


if __name__ == "__main__":
    # pt1
    crab_posns = [int(x) for x in read.read_file_as_list('y2021/day07/puzzle_input.csv')[0].split(',')]
    print(least_fuel_required(crab_posns))

    # pt2
    print(least_fuel_required_increase_burn_rate(crab_posns))
