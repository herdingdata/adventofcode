import pytest

from y2022.day03 import rucksack as r

@pytest.fixture()
def sample_rucksacks():
    return {
        1: "vJrwpWtwJgWrhcsFMMfFFhFp",
        2: "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        3: "PmmdzqPrVvPwwTWBwg",
        4: "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        5: "ttgJtRGJQctTZtZT",
        6: "CrZsJsPPZsGzwwsLwLmpwMDw",
    }


class TestCompartments:
    def test_compartments__their_sample1__expected_compartments(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[1])
        assert ruck.compartments == ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')

    def test_compartments__their_sample2__expected_compartments(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[2])
        assert ruck.compartments == ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL')

    def test_compartments__their_sample3__expected_compartments(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[3])
        assert ruck.compartments == ('PmmdzqPrV', 'vPwwTWBwg')

    def test_compartments__len_not_even__raises_value_error(self, sample_rucksacks):
        items = "abC"
        ruck = r.Rucksack(items)
        with pytest.raises(ValueError):
            compartments = ruck.compartments


class TestCommonItems:
    def test_common_items__sample1__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[1])
        assert ruck.common_items == "p"

    def test_common_items__sample2__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[2])
        assert ruck.common_items == "L"

    def test_common_items__sample3__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[3])
        assert ruck.common_items == "P"

    def test_common_items__sample4__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[4])
        assert ruck.common_items == "v"

    def test_common_items__sample5__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[5])
        assert ruck.common_items == "t"

    def test_common_items__sample6__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[6])
        assert ruck.common_items == "s"


class TestGetPrioritySum:
    def test_get_priority_sum__sample1__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[1])
        assert r.get_priority(ruck.common_items) == 16

    def test_get_priority_sum__sample2__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[2])
        assert r.get_priority(ruck.common_items) == 38

    def test_get_priority_sum__sample3__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[3])
        assert r.get_priority(ruck.common_items) == 42

    def test_get_priority_sum__sample4__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[4])
        assert r.get_priority(ruck.common_items) == 22

    def test_get_priority_sum__sample5__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[5])
        assert r.get_priority(ruck.common_items) == 20

    def test_get_priority_sum__sample6__expected(self, sample_rucksacks):
        ruck = r.Rucksack(sample_rucksacks[6])
        assert r.get_priority(ruck.common_items) == 19


def test_get_sum_of_all_common_item_priorities__their_sample__157(sample_rucksacks):
    rucksacks = list(sample_rucksacks.values())
    assert r.get_sum_of_all_common_item_priorities(rucksacks) == 157
