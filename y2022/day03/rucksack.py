import string
from collections.abc import Iterable
from itertools import islice
from dataclasses import dataclass

from helpers import read


_priorities_lcase = {l: idx + 1 for idx, l in enumerate(string.ascii_lowercase)}
_priorities_ucase = {l: idx + 27 for idx, l in enumerate(string.ascii_uppercase)}
PRIORITIES = _priorities_ucase | _priorities_lcase


def get_priority(items: str) -> int:
    return sum([PRIORITIES[item] for item in items])


@dataclass
class Rucksack:
    items: str

    _compartments: tuple = None
    _common_items: str = None

    @property
    def compartments(self):
        if self._compartments is None:
            num_items = len(self.items)
            if not (num_items % 2) == 0:
                raise ValueError("length of items is odd, expected it to be even")
            chunk_len = int(num_items / 2)
            comp1 = self.items[:chunk_len]
            comp2 = self.items[chunk_len:]
            self._compartments = (comp1, comp2)
        return self._compartments

    @property
    def common_items(self):
        if self._common_items is None:
            common_list = {item for item in self.compartments[0] if item in self.compartments[1]}
            self._common_items = ''.join(common_list)
        return self._common_items

    @property
    def item_set(self):
        return set(self.items)


def get_sum_of_all_common_item_priorities(items: list[str]) -> int:
    rucksacks = [Rucksack(i) for i in items]
    return sum([get_priority(r.common_items) for r in rucksacks])


def find_badge(rucksacks: Iterable[Rucksack]):
    return ''.join(set.intersection(*[r.item_set for r in rucksacks]))


def find_all_badges_points(items: list[str]):
    """
    items - the puzzle input, iterable of strings
    divides this input into chunks of 3, finds the badge for each
    return: sum of all the badge points
    """
    # pt2 - the rucksacks are in groups of 3, of which the matching item is the badge
    def _split_every(iterable: Iterable, n: int):  # thank you, SO https://stackoverflow.com/a/41200105/3911007
        iterable = iter(iterable)
        yield from iter(lambda: list(islice(iterable, n)), [])

    points = 0
    chunks_of_3 = _split_every(items, 3)
    for group_of_ruckitems in chunks_of_3:
        group_of_rucks = [Rucksack(it) for it in group_of_ruckitems]
        badge = find_badge(group_of_rucks)
        points += PRIORITIES[badge]
    return points


if __name__ == "__main__":
    # pt1
    rucks = [x for x in read.read_file_as_list('y2022/day03/puzzle_input.txt')]
    print(get_sum_of_all_common_item_priorities(rucks))

    # pt2
    print(find_all_badges_points(rucks))
