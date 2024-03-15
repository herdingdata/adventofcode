import numpy as np
import pytest

from y2023.day03 import gear_ratios as gr


@pytest.fixture()
def full_schema():
    return "467..114..\n" \
           "...*......\n" \
            "..35..633.\n" \
            "......#...\n" \
            "617*......\n" \
            ".....+.58.\n" \
            "..592.....\n" \
            "......755.\n" \
            "...$.*....\n" \
            ".664.598..\n"


@pytest.fixture()
def brief_schema():
    return "467..114..\n" \
           "...*......\n" \
            "..35..633.\n"


class TestEngineSchematic:
    def test_schematic_str(self, full_schema):
        # all numbers, regardless of whether they're a valid part
        schematic = gr.EngineSchematic(puzzle_input=full_schema)

        assert schematic.schematic_str == full_schema

    def test_schematic_array(self, brief_schema):
        # all numbers, regardless of whether they're a valid part
        # but this time we want the instances of PossiblePartNumbner
        expected_array = np.array([
            ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
            ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
        ])

        schematic = gr.EngineSchematic(puzzle_input=brief_schema)

        np.testing.assert_array_equal(schematic.schematic_array, expected_array)

    def test_symbols(self, brief_schema):
        # all numbers, regardless of whether they're a valid part
        # but this time we want the instances of PossiblePartNumbner
        expected_array = np.array([
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
        ])

        schematic = gr.EngineSchematic(puzzle_input=brief_schema)

        np.testing.assert_array_equal(schematic.is_sym_arr, expected_array)

    def test_all_possible_part_numbers(self, full_schema):
        # all numbers, regardless of whether they're a valid part
        expected_numbers = [467, 114, 35, 633, 617, 58, 592, 755, 664, 598]

        schematic = gr.EngineSchematic(puzzle_input=full_schema)

        assert schematic.all_possible_part_numbers == expected_numbers

    def test_all_possible_part_numbers_as_class_instances(self, brief_schema):
        # all numbers, regardless of whether they're a valid part
        # but this time we want the instances of PossiblePartNumbner
        expected_parts = [
            gr.PossiblePartNumber(value=467, start_xy=(0, 0), end_xy=(2, 0)),
            gr.PossiblePartNumber(value=114, start_xy=(5, 0), end_xy=(7, 0)),
            gr.PossiblePartNumber(value=35, start_xy=(2, 2), end_xy=(3, 2)),
            gr.PossiblePartNumber(value=633, start_xy=(6, 2), end_xy=(8, 2)),
        ]

        schematic = gr.EngineSchematic(puzzle_input=brief_schema)

        assert schematic.all_possible_parts == expected_parts

    def test_only_the_real_parts(self, full_schema):
        expected_parts = [467, 35, 633, 617, 592, 755, 664, 598]
        schematic = gr.EngineSchematic(puzzle_input=full_schema)

        result_instances = schematic.all_actual_parts
        result_nums = [x.value for x in result_instances]

        assert result_nums == expected_parts


class TestPossiblePartNumber:
    def test_params_stored_correctly(self):
        result_part = gr.PossiblePartNumber(value=467, start_xy=(0, 0), end_xy=(2, 0))
        assert result_part.value == 467
        assert result_part.start_xy == (0, 0)
        assert result_part.end_xy == (2, 0)

    @pytest.mark.parametrize('index,expected', [
        # (index from full list, expected bool)
        (0, True),  # 467
        (1, False),  # 114
        (2, True),  # 35
        (3, True),  # 633
        (4, True),  # 617
        (5, False),  # 58
        (6, True),  # 592
        (7, True),  # 755
        (8, True),  # 664
        (9, True),  # 598
    ])
    def test_is_real_part(self, full_schema, index, expected):
        schematic = gr.EngineSchematic(puzzle_input=full_schema)
        part = schematic.all_possible_parts[index]

        result = part.is_real_part(schematic.is_sym_arr)

        assert result == expected

    @pytest.mark.parametrize('index,expected', [
        # (index from full list, expected bool)
        (0, True),  # 467
        (1, False),  # 114
        (2, True),  # 35
        (3, False),  # 633
        (4, False),  # 617
        (5, False),  # 58
        (6, False),  # 592
        (7, True),  # 755
        (8, False),  # 664
        (9, True),  # 598
    ])
    def test_is_gear_part(self, full_schema, index, expected):
        schematic = gr.EngineSchematic(puzzle_input=full_schema)
        part = schematic.all_possible_parts[index]

        result = part.is_gear_part(schematic.is_ast_arr)

        assert result == expected


