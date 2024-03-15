import pytest

from y2023.day04 import scratchcards


@pytest.mark.parametrize('game_definition,expected', [
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", {41, 48, 83, 86, 17}),
    ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", {13, 32, 20, 16, 61}),
    ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", {1, 21, 53, 59, 44}),
    ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", {41, 92, 73, 84, 69}),
    ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", {87, 83, 26, 28, 32}),
    ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", {31, 18, 13, 56, 72}),
])
def test__extract_winners(game_definition: str, expected: int):
    assert scratchcards.extract_winners(game_definition) == expected


@pytest.mark.parametrize('game_definition,expected', [
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", {83, 86,  6, 31, 17,  9, 48, 53}),
    ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", {61, 30, 68, 82, 17, 32, 24, 19}),
    ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", {69, 82, 63, 72, 16, 21, 14,  1}),
    ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", {59, 84, 76, 51, 58,  5, 54, 83}),
    ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", {88, 30, 70, 12, 93, 22, 82, 36}),
    ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", {74, 77, 10, 23, 35, 67, 36, 11}),
])
def test__extract_game(game_definition: str, expected: int):
    assert scratchcards.extract_game(game_definition) == expected


@pytest.mark.parametrize('game_definition,expected', [
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 0),
    ("Card 126: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 125),
])
def test__extract_index(game_definition: str, expected: int):
    assert scratchcards.extract_index(game_definition) == expected


@pytest.mark.parametrize('game_definition,expected', [
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
    ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
    ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
    ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
    ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
    ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
])
def test_pt1__get_score_for_game(game_definition: str, expected: int):
    assert scratchcards.get_score_for_game(game_definition) == expected


@pytest.mark.parametrize('game_definition,expected', [
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 4),
    ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
    ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
    ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
    ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
    ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
])
def test_pt1__count_matches(game_definition: str, expected: int):
    game = scratchcards.extract_all(game_definition)
    assert scratchcards.count_matches_for_game(game) == expected


@pytest.fixture()
def six_games():
    return [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]


def test_pt1__sum_scores_for_games(six_games):
    assert scratchcards.sum_scores_for_games(six_games) == 13


def test_pt2__count_won_scratchcards(six_games):
    games = six_games

    assert scratchcards.count_won_scratchcards(games) == 30


def test_pt2__is_there_a_win_false():
    game_strs = [
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
    games = [scratchcards.extract_all(g) for g in game_strs]

    assert scratchcards.is_there_a_winner(games) is False


def test_pt2__is_there_a_winner_true(six_games):
    games = [scratchcards.extract_all(g) for g in six_games]
    assert scratchcards.is_there_a_winner(games) is True
