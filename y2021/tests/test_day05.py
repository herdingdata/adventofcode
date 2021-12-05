from y2021.day05 import hydrothermal_venture as hv


def test_get_coords_of_line__their_sample_row1__produces_expected():
    sample_input = "0,9 -> 5,9"
    expected_line = ((0, 9), (5, 9))
    result_line = hv.get_coords_of_line(sample_input)
    assert result_line == expected_line


def test_get_coords_of_line__their_sample_row1__produces_expected():
    sample_input = "8,0 -> 0,8"
    expected_line = ((8, 0), (0, 8))
    result_line = hv.get_coords_of_line(sample_input)
    assert result_line == expected_line


def test_get_points_covered_by_line__their_sample_1__produces_expected():
    sample_start = (1, 1)
    sample_finish = (1, 3)
    expected_points = [(1, 1), (1, 2), (1, 3)]
    result_points = hv.get_points_covered_by_line(sample_start, sample_finish, ignore_diagonals=True)
    assert result_points == expected_points


def test_get_points_covered_by_line__their_sample_2__produces_expected():
    sample_start = (9, 7)
    sample_finish = (7, 7)
    expected_points = [(9, 7), (8, 7), (7, 7)]
    result_points = hv.get_points_covered_by_line(sample_start, sample_finish, ignore_diagonals=True)
    assert result_points == expected_points


def test_get_points_covered_by_line__diagonal_x_increases_y_decreases__produces_expected():
    sample_start = (1, 9)
    sample_finish = (3, 7)
    expected_points = [(1, 9), (2, 8), (3, 7)]
    result_points = hv.get_points_covered_by_line(sample_start, sample_finish, ignore_diagonals=False)
    assert result_points == expected_points


def test_get_points_covered_by_line__a_diagonal__produces_expected():
    sample_start = (7, 7)
    sample_finish = (9, 9)
    expected_points = [(7, 7), (8, 8), (9, 9)]
    result_points = hv.get_points_covered_by_line(sample_start, sample_finish, ignore_diagonals=False)
    assert result_points == expected_points


def test_get_points_covered_by_line__ignore_diagonal__returns_empty_list():
    sample_start = (1, 1)
    sample_finish = (3, 3)
    expected_points = []
    result_points = hv.get_points_covered_by_line(sample_start, sample_finish, ignore_diagonals=True)
    assert result_points == expected_points


def test_count_overlapping_points__their_sample__produces_expected():
    sample_input = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]
    expected_overlaps = 5
    result_overlaps = hv.get_overlaps(sample_input, ignore_diagonals=True)
    assert result_overlaps == expected_overlaps
