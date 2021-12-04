from y2021.day04 import bingo


def test__get_numbers_and_boards__their_sample():
    sample_input = [
        "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
        "",
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
        "",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
    ]
    expected_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    expected_board_1 = [
        [22,13,17,11,0],
        [8,2,23,4,24],
        [21,9,14,16,7],
        [6,10,3,18,5],
        [1,12,20,15,19],
    ]
    expected_board_2 = [
        [3,15,0,2,22],
        [9,18,13,17,5],
        [19,8,7,25,23],
        [20,11,10,24,4],
        [14,21,16,12,6],
    ]
    result_numbers, result_boards = bingo.get_numbers_and_boards(sample_input)
    assert result_numbers == expected_numbers
    assert result_boards[0] == expected_board_1
    assert result_boards[1] == expected_board_2


def test__turn_board_into_called_dict():
    sample_board = [
            [22,13,17,11,0],
            [8,2,23,4,24],
            [21,9,14,16,7],
            [6,10,3,18,5],
            [1,12,20,15,19],
    ]
    expected_board = [
        {22: False, 13: False, 17: False, 11: False, 0: False},
        {8: False, 2: False, 23: False, 4: False, 24: False},
        {21: False, 9: False, 14: False, 16: False, 7: False},
        {6: False, 10: False, 3: False, 18: False, 5: False},
        {1: False, 12: False, 20: False, 15: False, 19: False},
    ]
    result_board = bingo.turn_board_into_called_dict(sample_board)
    assert result_board == expected_board


def test_get_tally_of_board():
    sample_board = [
        {14: True, 21: True, 17: True, 24: True, 4: True},
        {10: False, 16: False, 15: False, 9: True, 19: False},
        {18: False, 8: False, 23: True, 26: False, 20: False},
        {22: False, 11: True, 13: False, 6: False, 5: True},
        {2: True, 0: True, 12: False, 3: False, 7: True},
    ]
    expected_tally = 188
    result_tally = bingo.get_tally_of_board(sample_board)
    assert result_tally == expected_tally


def test_is_row_full__true():
    sample_board = [
        {14: True, 21: True, 17: True, 24: True, 4: True},
        {10: False, 16: False, 15: False, 9: True, 19: False},
        {18: False, 8: False, 23: True, 26: False, 20: False},
        {22: False, 11: True, 13: False, 6: False, 5: True},
        {2: True, 0: True, 12: False, 3: False, 7: True},
    ]
    result_is_full = bingo.is_row_full(sample_board, row_idx=0)
    assert result_is_full is True


def test_is_row_full__false():
    sample_board = [
        {14: True, 21: True, 17: True, 24: True, 4: True},
        {10: False, 16: False, 15: False, 9: False, 19: False},
        {18: False, 8: False, 23: True, 26: False, 20: False},
        {22: False, 11: False, 13: False, 6: False, 5: False},
        {2: False, 0: False, 12: False, 3: False, 7: False},
    ]
    result_is_full = bingo.is_row_full(sample_board, row_idx=2)
    assert result_is_full is False


def test_is_col_full__true():
    sample_board = [
        {14: False, 21: True, 17: False, 24: False, 4: False},
        {10: False, 16: True, 15: False, 9: False, 19: False},
        {18: False, 8: True, 23: False, 26: False, 20: False},
        {22: False, 11: True, 13: False, 6: False, 5: False},
        {2: False, 0: True, 12: False, 3: False, 7: False},
    ]
    result_is_full = bingo.is_col_full(sample_board, col_idx=1)
    assert result_is_full is True


def test_is_col_full__false():
    sample_board = [
        {14: False, 21: True, 17: False, 24: False, 4: False},
        {10: False, 16: True, 15: False, 9: False, 19: False},
        {18: False, 8: True, 23: False, 26: False, 20: False},
        {22: False, 11: True, 13: False, 6: False, 5: False},
        {2: True, 0: True, 12: False, 3: False, 7: False},
    ]
    result_is_full = bingo.is_col_full(sample_board, col_idx=0)
    assert result_is_full is False


def test__get_score_winner__their_sample():
    sample_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    sample_boards = [
        [
            [22,13,17,11,0],
            [8,2,23,4,24],
            [21,9,14,16,7],
            [6,10,3,18,5],
            [1,12,20,15,19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14,21,17,24,4],
            [10,16,15,9,19],
            [18,8,23,26,20],
            [22,11,13,6,5],
            [2,0,12,3,7],
        ],
    ]
    expected_score = 4512
    result_score = bingo.find_score_of_winner(sample_numbers, sample_boards)
    assert result_score == expected_score


def test__get_score_loser__their_sample():
    sample_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    sample_boards = [
        [
            [22,13,17,11,0],
            [8,2,23,4,24],
            [21,9,14,16,7],
            [6,10,3,18,5],
            [1,12,20,15,19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14,21,17,24,4],
            [10,16,15,9,19],
            [18,8,23,26,20],
            [22,11,13,6,5],
            [2,0,12,3,7],
        ],
    ]
    expected_score = 1924
    result_score = bingo.find_score_of_loser(sample_numbers, sample_boards)
    assert result_score == expected_score
