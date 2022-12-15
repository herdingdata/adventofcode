from helpers import read

OPTIONS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
OPPONENT = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}
ME = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}
DESIRE = {
    'X': False, # lose
    'Y': None,  # draw
    'Z': True,  # win
}
# pt2
WINNERS = {
    # if you have a rock{key} you need to play paper{value} to win
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock',
}
LOSERS = {v: k for k, v in WINNERS.items()}


def did_i_win(opponent_choice, my_choice) -> bool:
    """
    return: true if win; false if lose; None if draw
    """
    if opponent_choice == my_choice:
        return None
    opp_points = OPTIONS[opponent_choice]
    my_points = OPTIONS[my_choice]
    # if we're playing rock v scissors, rock wins because it's smaller
    if (opp_points == 1 and my_points == 3) or (opp_points == 3 and my_points == 1):
        return my_points < opp_points
    # else which is greater
    return my_points > opp_points


def play_games_and_calc_points(games, convert_from_letters=True):
    opp_score = 0
    my_score = 0
    for game in games:
        if convert_from_letters:
            opp_choice, my_choice = get_game_choices_as_words(game)
        else:
            opp_choice, my_choice = game.split(' ')
        result = did_i_win(opp_choice, my_choice)
        opp_score += OPTIONS[opp_choice]
        my_score += OPTIONS[my_choice]
        if result is not None:
            if result:
                my_score += 6
            else:
                opp_score += 6
        else: # draw
            my_score += 3
            opp_score += 3
    return (opp_score, my_score)


def get_game_choices_as_words(game, pt2=False):
    opp_choice_letter, my_choice_letter = game.split(' ')
    opp_choice = OPPONENT[opp_choice_letter]
    if pt2 is True:
        # my choice letter is desired outcome
        my_choice = DESIRE[my_choice_letter]
    else:
        # else my choice is a rock/paper/scissors
        my_choice = ME[my_choice_letter]
    return opp_choice, my_choice


def get_choice_to_match_desired_outcome(opp_choice: str, desired: bool):
    if desired is None:
        return opp_choice
    if desired:
        return WINNERS[opp_choice]
    return LOSERS[opp_choice]


def work_out_games_to_match_strategy(in_games: list[str]) -> list:
    """
    in_games: ['A X', 'B Y']
    out_games: ['rock False'
    """
    out_games = []
    for game in in_games:
        opp_choice, desired_outcome = get_game_choices_as_words(game, pt2=True)
        my_choice = get_choice_to_match_desired_outcome(opp_choice, desired_outcome)
        out_games.append(f'{opp_choice} {my_choice}')
    return out_games


if __name__ == "__main__":
    # pt1
    games = [x for x in read.read_file_as_list('y2022/day02/puzzle_input.txt')]
    _, me = play_games_and_calc_points(games)
    print(f'pt1: my score is {me}')

    # pt2
    pt2_games = work_out_games_to_match_strategy(games)
    _, me2 = play_games_and_calc_points(pt2_games, convert_from_letters=False)
    print(f'pt2: my score is {me2}')
