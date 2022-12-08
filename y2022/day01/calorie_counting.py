from helpers import read


def get_elves_calories(calory_list: list[str]) -> list[list[int]]:
    elves = []
    current_elf = []
    for calory in calory_list:
        if calory == '':
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(calory))
    elves.append(current_elf)
    return elves


def summarise_elves(elf_lists: list[list[int]]) -> list[int]:
    return [sum(e) for e in elf_lists]


def fattest_elfs_calories(calory_list: list[str]) -> int:
    elves = get_elves_calories(calory_list)
    summaries = summarise_elves(elves)
    return max(summaries)


def fattest_three_elves_calories(calory_list: list[str]) -> int:
    elves = get_elves_calories(calory_list)
    top3 = sorted(summarise_elves(elves), reverse=True)[:3]
    return sum(top3)


if __name__ == "__main__":
    calories = [x for x in read.read_file_as_list('y2022/day01/puzzle_input.txt')]
    print(fattest_elfs_calories(calories))
    print(fattest_three_elves_calories(calories))
