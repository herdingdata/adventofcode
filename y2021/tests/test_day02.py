from y2021.day02 import pilot_this_thing


class TestPart1:
    def test__pilot_this_thing__their_sample__returns_expected(self):
        sample_commands = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]
        expected_depth = 10
        expected_horiz = 15

        result_horiz, result_depth = pilot_this_thing.pilot_the_sub(sample_commands)
        assert result_horiz == expected_horiz
        assert result_depth == expected_depth


    def test__pilot_this_thing__just_forward__returns_expected(self):
        sample_commands = [
            'forward 5',
        ]
        expected_depth = 0
        expected_horiz = 5

        result_horiz, result_depth = pilot_this_thing.pilot_the_sub(sample_commands)
        assert result_horiz == expected_horiz
        assert result_depth == expected_depth


    def test__pilot_this_thing__just_down__returns_expected(self):
        sample_commands = [
            'down 7',
        ]
        expected_depth = 7
        expected_horiz = 0

        result_horiz, result_depth = pilot_this_thing.pilot_the_sub(sample_commands)
        assert result_horiz == expected_horiz
        assert result_depth == expected_depth


    def test__pilot_this_thing__down_then_up__returns_expected(self):
        sample_commands = [
            'down 5',
            'up 3',
        ]
        expected_depth = 2
        expected_horiz = 0

        result_horiz, result_depth = pilot_this_thing.pilot_the_sub(sample_commands)
        assert result_horiz == expected_horiz
        assert result_depth == expected_depth


class TestPartTwo:
    def test__pilot_with_aim__their_sample__returns_expected(self):
        sample_commands = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]
        expected_depth = 60
        expected_horiz = 15

        result_horiz, result_depth = pilot_this_thing.pilot_with_aim(sample_commands)
        assert result_horiz == expected_horiz
        assert result_depth == expected_depth
