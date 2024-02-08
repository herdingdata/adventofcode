from y2023.day02.cube_conundrum import CubeGame, CubeSet, CubeBag, sum_possible_games, sum_minimum_viable_sets


class TestSet:
    def test__from_text(self):
        expected_set = CubeSet(r=1, g=2, b=6)
        result_set = CubeSet.from_text("1 red, 2 green, 6 blue")
        assert result_set == expected_set

    def test__power_game1_min_viable_set(self):
        sample_set = CubeSet.from_text("4 red, 2 green, 6 blue")
        result_power = sample_set.power
        assert result_power == 48

    def test__power_game2_min_viable_set(self):
        sample_set = CubeSet.from_text("1 red, 3 green, 4 blue")
        result_power = sample_set.power
        assert result_power == 12

    def test__power_game3_min_viable_set(self):
        sample_set = CubeSet.from_text("20 red, 13 green, 6 blue")
        result_power = sample_set.power
        assert result_power == 1560

    def test__power_game4_min_viable_set(self):
        sample_set = CubeSet.from_text("14 red, 3 green, 15 blue")
        result_power = sample_set.power
        assert result_power == 630

    def test__power_game5_min_viable_set(self):
        sample_set = CubeSet.from_text("6 red, 3 green, 2 blue")
        result_power = sample_set.power
        assert result_power == 36


class TestGame:
    def test_init__stores_all_attrs(self):
        intext = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected_sets = [CubeSet(b=3, r=4), CubeSet(r=1, g=2, b=6), CubeSet(g=2)]

        game = CubeGame(text_description=intext)

        assert game.id == 1
        assert game.sets == expected_sets

    def test_sample_games__are_possible(self):
        game1 = CubeGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        game2 = CubeGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        game5 = CubeGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        sample_bag = CubeBag(r=12, g=13, b=14)

        is_1_possible = sample_bag.is_game_possible(game1)
        is_2_possible = sample_bag.is_game_possible(game2)
        is_5_possible = sample_bag.is_game_possible(game5)

        assert is_1_possible is True
        assert is_2_possible is True
        assert is_5_possible is True

    def test_sample_games__are_not_possible(self):
        game3 = CubeGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        game4 = CubeGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        sample_bag = CubeBag(r=12, g=13, b=14)

        is_3_possible = sample_bag.is_game_possible(game3)
        is_4_possible = sample_bag.is_game_possible(game4)

        assert is_3_possible is False
        assert is_4_possible is False


class TestGameMinimumSet:
    """
    we're still testing Game class, but this is grouping several tests relating to the minimum set required
    in other words: part 2
    """
    def test_game1(self):
        cube_game = CubeGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        expected_min_set = CubeSet.from_text("4 red, 2 green, 6 blue")

        result_min_set = cube_game.minimum_viable_set

        assert result_min_set == expected_min_set

    def test_game2(self):
        cube_game = CubeGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        expected_min_set = CubeSet.from_text("1 red, 3 green, 4 blue")

        result_min_set = cube_game.minimum_viable_set

        assert result_min_set == expected_min_set

    def test_game3(self):
        cube_game = CubeGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        expected_min_set = CubeSet.from_text("20 red, 13 green, 6 blue")

        result_min_set = cube_game.minimum_viable_set

        assert result_min_set == expected_min_set

    def test_game4(self):
        cube_game = CubeGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        expected_min_set = CubeSet.from_text("14 red, 3 green, 15 blue")

        result_min_set = cube_game.minimum_viable_set

        assert result_min_set == expected_min_set

    def test_game5(self):
        cube_game = CubeGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        expected_min_set = CubeSet.from_text("6 red, 3 green, 2 blue")

        result_min_set = cube_game.minimum_viable_set

        assert result_min_set == expected_min_set


def test_sum_of_possible_games():
    sample_bag = CubeBag(r=12, g=13, b=14)
    sample_games = [
        CubeGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
        CubeGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"),
        CubeGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"),
        CubeGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"),
        CubeGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"),
    ]
    result = sum_possible_games(sample_bag, sample_games)
    assert result == 8  # 1 + 2 + 5


def test_sum_of_minimum_viable_sets():
    sample_games = [
        CubeGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
        CubeGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"),
        CubeGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"),
        CubeGame("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"),
        CubeGame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"),
    ]
    result = sum_minimum_viable_sets(sample_games)
    assert result == 2286
