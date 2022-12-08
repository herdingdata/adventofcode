from helpers import read


def turn_fish_list_into_summarised_dict(fish_counters: list) -> dict:
    summary_dict = {}
    for fish_days in fish_counters:
        if fish_days in summary_dict:
            summary_dict[fish_days] += 1
        else:
            summary_dict[fish_days] = 1
    return summary_dict


def simulate_lanternfish(fish_counters: list, num_days: int) -> list:
    count_dict = turn_fish_list_into_summarised_dict(fish_counters)
    for day_idx in range(0, num_days):
        tomorrow_dict = {}
        for days_until_pop, count in count_dict.items():
            print(f"{day_idx=}, {days_until_pop=}, {count=}")
            if days_until_pop == 0:
                tomorrow_dict[8] = count
                if 6 in tomorrow_dict:
                    tomorrow_dict[6] += count
                else:
                    tomorrow_dict[6] = count
            elif days_until_pop - 1 in tomorrow_dict:
                # we've already added day 6 to dict
                tomorrow_dict[days_until_pop - 1] += count
            else:
                tomorrow_dict[days_until_pop - 1] = count
        count_dict = tomorrow_dict
    return count_dict


def count_lanternfish(fish_counters: list, num_days: int) -> int:
    lanterns = simulate_lanternfish(fish_counters, num_days)
    return sum([v for v in lanterns.values()])


if __name__ == "__main__":
    starting_lanterns = [int(x) for x in read.read_file_as_list('y2021/day06/puzzle_input.csv')[0].split(',')]
    print(count_lanternfish(fish_counters=starting_lanterns, num_days=80))

    print(count_lanternfish(fish_counters=starting_lanterns, num_days=256))
