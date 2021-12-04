from typing import List
from itertools import islice

from y2021.helpers import read


def get_numbers_and_boards(data: List[str]) -> (int, List[List[int]]):
    numbers = [int(x) for x in data[0].split(',')]
    boards = []
    for idx in range(2, len(data) - 4, 6):
        boards.append([[int(a) for a in row.split()] for row in islice(data, idx, idx + 5)])
    return numbers, boards


def turn_board_into_called_dict(board):
    new_board = []
    for row in board:
        new_board.append({x: False for x in row})
    return new_board


def get_tally_of_board(board_w_status) -> int:
    """
    give this a board with dicts of {int: True|False} for each row
    then it will add up all the numbers which are false
    """
    tally = 0
    for row in board_w_status:
        for number, called_bool in row.items():
            if called_bool is False:
                tally += number
    return tally


def find_score_of_winner(numbers: List[int], boards: List[List[List[int]]]):
    boards_w_status = [turn_board_into_called_dict(b) for b in boards]
    for number_called in numbers:
        for brd_idx, board in enumerate(boards_w_status):
            for row_idx, row in enumerate(board):
                if number_called in row:
                    boards_w_status[brd_idx][row_idx][number_called] = True
                board_copy = boards_w_status[brd_idx]
                col_idx = get_col_index(row, number_called)
                if is_row_full(board_copy, row_idx) or is_col_full(board_copy, col_idx):
                    score = get_tally_of_board(board) * number_called
                    return score


def is_row_full(board, row_idx):
    return all(board[row_idx].values())


def is_col_full(board, col_idx):
    if col_idx is None:
        return False
    values = []
    for row in board:
        values.append([x for x in islice(row.values(), col_idx, col_idx + 1)][0])
    return all(values)


def get_col_index(row, number_called):
    try:
        return list(row.keys()).index(number_called)
    except ValueError:
        return None


def find_score_of_loser(numbers: List[int], boards: List[List[List[int]]]):
    boards_w_status = [turn_board_into_called_dict(b) for b in boards]
    board_scores = {idx: None for idx, _ in enumerate(boards_w_status)}
    for number_called in numbers:
        for brd_idx, board in enumerate(boards_w_status):
            if board_scores[brd_idx] is None:
                for row_idx, row in enumerate(board):
                    if number_called == 13:
                        print(1)
                    if number_called in row:
                        boards_w_status[brd_idx][row_idx][number_called] = True
                    board_copy = boards_w_status[brd_idx]
                    col_idx = get_col_index(row, number_called)
                    if is_row_full(board_copy, row_idx) or is_col_full(board_copy, col_idx):
                        score = get_tally_of_board(board) * number_called
                        board_scores[brd_idx] = score
                        last_board_to_win = brd_idx
    return board_scores[last_board_to_win]


if __name__ == "__main__":
    # pt1
    numbers, boards = get_numbers_and_boards(read.read_file_as_list('y2021/day04/puzzle_input.csv'))
    score = find_score_of_winner(numbers, boards)
    print(score)

    # pt2
    print(find_score_of_loser(numbers, boards))
