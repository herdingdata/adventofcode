import re
from collections import namedtuple
from typing import Iterable, Set, Tuple

from helpers import read


Game = namedtuple("Game", "win played index")  # set, set, int

WINNERS_RE = re.compile(r"(?<=\:)[\d ]+(?=\|)")
GAME_RE = re.compile(r"(?<=\|)[\d ]+$")
CARD_NUM = re.compile(r"Card[ ]+([\d ]+)(?=\:)")


def extract_winners(game_definition) -> Set[int]:
    """
    the set of numbers which represents the winning numbers
    """
    winners_str = WINNERS_RE.search(game_definition).group(0).strip()
    winners = set([int(w) for w in winners_str.split()])
    return winners


def extract_game(game_definition: str) -> Set[int]:
    """
    the set of numbers which represents the numbers played
    """
    game_str = GAME_RE.search(game_definition).group(0).strip()
    return set([int(w) for w in game_str.split()])


def extract_index(game_definition: str) -> int:
    """
    zero based index of the card number
    """
    return int(CARD_NUM.search(game_definition).group(1)) - 1


def extract_all(game_definition: str) -> Game:
    return Game(win=extract_winners(game_definition), played=extract_game(game_definition),
                index=extract_index(game_definition))


def count_matches_for_game(game: Game):
    return len(game.win.intersection(game.played))


def get_score_for_game(game_definition: str) -> int:
    """
    :game_definition: a full row of the puzzle input
    """
    # print(game_definition)  # debug
    game = extract_all(game_definition)
    num_matches = count_matches_for_game(game)
    if num_matches == 1:
        return 1
    if num_matches > 1:
        points = 1
        for idx in range(2, num_matches + 1):
            points *= 2  # I'm sure there's a neater mathematical way of doing this: binary
        return points
    return 0


def sum_scores_for_games(game_definitions: Iterable[str]) -> int:
    """
    :game_definition: an iterable of strings, each of which is a full row of the puzzle input
    """
    return sum([get_score_for_game(x) for x in game_definitions])


def is_there_a_winner(game_definitions: Game) -> bool:
    """
    if one of the games has any wins, return true as early/cheaply as poss
    """
    for game in game_definitions:
        if count_matches_for_game(game) > 0:
            return True
    return False


def _count_won_scratchcards(game_definitions_evaluated: Iterable[Game], game_definitions_all: Iterable[Game], depth: int) -> int:
    """
    the recursive bit; which doesn't include the original cards
    again, I'm sure there's a far more efficient way of doing this
    challenge for future me: make it fast

    game_definitions_evaluated: list of tuple (winners set, game set, index)
    game_definitions_all: list of tuple (winners set, game set) exactly as per puzzle

    idea: learn about async but pycharm started 140 odd threads so arguable how much it'll help
    idea: keep the card numbers separate so I'm not regexing them upon every loop
    idea: tail recursive loop
    """
    depth += 1
    print(f"inception level {depth}, num records evaluated {len(game_definitions_evaluated)}")
    copied_cards = []
    for game in game_definitions_evaluated:
        idx = game.index
        count = count_matches_for_game(game)
        copied_cards.extend(game_definitions_all[idx + 1: idx + 1 + count])
    total = len(copied_cards)
    if is_there_a_winner(copied_cards):
        total += _count_won_scratchcards(copied_cards, game_definitions_all, depth)
    depth -= 1
    return total


def count_won_scratchcards(game_definitions: Iterable[str]) -> int:
    """
    we're on pt2 now
    how many scratchcards did we win as a result of games being won
    """
    depth = 0
    game_list = [extract_all(g) for g in game_definitions]
    return _count_won_scratchcards(game_list, game_list, depth) + len(game_definitions)


if __name__ == "__main__":
    puzzle = read.read_file_as_list('y2023/day04/puzzle_input.txt')

    pt1_sum = sum_scores_for_games(puzzle)
    print(f"pt1: sum of all scores {pt1_sum}")

    pt2_sum = count_won_scratchcards(puzzle)
    print(f"pt2: sum of all scores {pt2_sum}")


