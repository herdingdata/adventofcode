from y2021.day06 import exponential_lanternfish as el


def test__turn_fish_list_into_summarised_dict__their_sample_18_days__produces_expected():
    sample_lanterns = [3,4,3,1,2]
    expected_lanterns = {1: 1, 2: 1, 3: 2, 4: 1}
    result_lanterns = el.turn_fish_list_into_summarised_dict(sample_lanterns)
    assert result_lanterns == expected_lanterns


def test__simulate_lanternfish__their_sample_5_days__produces_expected():
    sample_lanterns = [3]
    sample_num_days = 5
    expected_lanterns = {7: 1, 5: 1}
    result_lanterns = el.simulate_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns


def test__simulate_lanternfish__their_sample_18_days_pt1__produces_expected():
    sample_lanterns = [3,4,3,1,2]
    sample_num_days = 1
    expected_lanterns = {0: 1, 1: 1, 2: 2, 3: 1}
    result_lanterns = el.simulate_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns


def test__simulate_lanternfish__their_sample_18_days_pt2__produces_expected():
    sample_lanterns = [3,4,3,1,2]
    sample_num_days = 2
    expected_lanterns = {0: 1, 1: 2, 2: 1, 6: 1, 8: 1}
    result_lanterns = el.simulate_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns


def test__simulate_lanternfish__their_sample_18_days_pt3__produces_expected():
    sample_lanterns = [3,4,3,1,2]
    sample_num_days = 3
    expected_lanterns = {6: 1, 0: 2, 1: 1, 5: 1, 7: 1, 8: 1}
    result_lanterns = el.simulate_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns


def test__count_lanternfish__their_sample_18_days__produces_expected():
    sample_lanterns = [3,4,3,1,2]
    sample_num_days = 18
    expected_lanterns = 26
    result_lanterns = el.count_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns


def test__count_lanternfish__their_sample_80_days__produces_expected():
    sample_lanterns = [3, 4, 3, 1, 2]
    sample_num_days = 80
    expected_lanterns = 5934
    result_lanterns = el.count_lanternfish(sample_lanterns, num_days=sample_num_days)
    assert result_lanterns == expected_lanterns
