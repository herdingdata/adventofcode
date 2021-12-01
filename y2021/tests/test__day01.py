from y2021.day01 import depth_readings


def test__count_increments__with_their_sample__returns_expected():
    sample_readings = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_increments = 7

    result = depth_readings.count_increments(sample_readings)

    assert result == expected_increments


def test__get_sum_of_three_readings__with_first_3__returns_expected():
    sample_readings = [199, 200, 208, 210, 200]
    start = 0
    expected = 199 + 200 + 208

    result = depth_readings.get_sum_of_3_readings(sample_readings, 0)

    assert result == expected


def test__blocks_of_three__with_their_sample__returns_expected():
    sample_readings = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected_increments = 5

    result = depth_readings.count_increments_across_3_readings(sample_readings)

    assert result == expected_increments
