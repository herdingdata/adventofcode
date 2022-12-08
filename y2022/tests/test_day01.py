from y2022.day01 import calorie_counting as cc


def test_get_elves():
    input = ['1', '2', '', '3']
    assert cc.get_elves_calories(input) == [[1, 2], [3]]


def test_summarise_elves():
    input = [[1, 2, 3], [3]]
    assert cc.summarise_elves(input) == [6, 3]


def test_fattest_elfs_calories():
    input = ['1', '2', '3', '', '3']
    assert cc.fattest_elfs_calories(input) == 6


def test_fattest_three_elves_calories():
    input = ['1', '', '2', '', '3', '', '4', '5']
    assert cc.fattest_three_elves_calories(input) == 14
