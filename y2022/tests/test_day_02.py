from y2022.day02 import rock_paper_scissors as rps


class TestDidIWin:
    def test_rock_rock__draw(self):
        opponent_choice = 'rock'
        my_choice = 'rock'
        assert rps.did_i_win(opponent_choice, my_choice) is None

    def test_rock_scissors__lose(self):
        opponent_choice = 'rock'
        my_choice = 'scissors'
        assert rps.did_i_win(opponent_choice, my_choice) is False

    def test_rock_paper__win(self):
        opponent_choice = 'rock'
        my_choice = 'paper'
        assert rps.did_i_win(opponent_choice, my_choice)  is True

    def test_paper_paper__draw(self):
        opponent_choice = 'paper'
        my_choice = 'paper'
        assert rps.did_i_win(opponent_choice, my_choice) is None

    def test_paper_rock__lose(self):
        opponent_choice = 'paper'
        my_choice = 'rock'
        assert rps.did_i_win(opponent_choice, my_choice) is False

    def test_paper_scissors__win(self):
        opponent_choice = 'paper'
        my_choice = 'scissors'
        assert rps.did_i_win(opponent_choice, my_choice) is True

    def test_scissors_scissors__draw(self):
        opponent_choice = 'scissors'
        my_choice = 'scissors'
        assert rps.did_i_win(opponent_choice, my_choice) is None

    def test_scissors_rock__win(self):
        opponent_choice = 'scissors'
        my_choice = 'rock'
        assert rps.did_i_win(opponent_choice, my_choice) is True

    def test_scissors_paper__lose(self):
        opponent_choice = 'scissors'
        my_choice = 'paper'
        assert rps.did_i_win(opponent_choice, my_choice) is False


class TestGetGamesChoicesAsWords:
    def test_pt1_a_y__returns_rock_paper(self):
        game = "A Y"
        opp, me = rps.get_game_choices_as_words(game)
        assert opp == "rock"
        assert me == "paper"

    def test_pt1_b_z__returns_paper_scissors(self):
        game = "B Z"
        opp, me = rps.get_game_choices_as_words(game)
        assert opp == "paper"
        assert me == "scissors"

    def test_pt2_a_x__returns_rock_lose(self):
        game = "A X"
        opp, me = rps.get_game_choices_as_words(game, pt2=True)
        assert opp == "rock"
        assert me is False

    def test_pt2_a_y__returns_rock_draw(self):
        game = "A Y"
        opp, me = rps.get_game_choices_as_words(game, pt2=True)
        assert opp == "rock"
        assert me is None

    def test_pt2_a_z__returns_rock_win(self):
        game = "A Z"
        opp, me = rps.get_game_choices_as_words(game, pt2=True)
        assert opp == "rock"
        assert me is True


class TestGetChoiceToMatchDesiredOutcome:
    # draw
    def test_rock_draw__returns_rock(self):
        opp = 'rock'
        desired = None
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'rock'

    def test_scissors_draw__returns_scissors(self):
        opp = 'scissors'
        desired = None
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'scissors'

    def test_paper_draw__returns_paper(self):
        opp = 'paper'
        desired = None
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'paper'

    # win
    def test_rock_win__returns_paper(self):
        opp = 'rock'
        desired = True
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'paper'

    def test_scissors_win__returns_rock(self):
        opp = 'scissors'
        desired = True
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'rock'

    def test_paper_win__returns_scissors(self):
        opp = 'paper'
        desired = True
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'scissors'

    # lose
    def test_rock_lose__returns_scissors(self):
        opp = 'rock'
        desired = False
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'scissors'

    def test_scissors_lose__returns_paper(self):
        opp = 'scissors'
        desired = False
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'paper'

    def test_paper_lose__returns_rock(self):
        opp = 'paper'
        desired = False
        result = rps.get_choice_to_match_desired_outcome(opp, desired)
        assert result == 'rock'


def test_work_out_games_to_match_strategy__their_sample__return_expected():
    games = [
        'A Y',
        'B X',
        'C Z',
    ]
    expected = [
        'rock rock',
        'paper rock',
        'scissors rock',
    ]
    result = rps.work_out_games_to_match_strategy(games)
    assert result == expected


class TestPlayGamesAndCalcPoints:
    def test_their_pt1_sample__expected_points(self):
        games = [
            'A Y',
            'B X',
            'C Z',
        ]
        result_opp, result_me = rps.play_games_and_calc_points(games)
        assert result_me == 15

    def test_their_pt2_sample__return_expected(self):
        games = [
            'A Y',
            'B X',
            'C Z',
        ]
        desired_games = rps.work_out_games_to_match_strategy(games)  # technical an int test, not a unittest
        result_opp, result_me = rps.play_games_and_calc_points(desired_games, convert_from_letters=False)
        assert result_me == 12
