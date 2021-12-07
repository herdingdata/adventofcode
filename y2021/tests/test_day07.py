import pytest
from collections import namedtuple

from y2021.day07 import pesky_whales


def test__least_fuel_required__their_sample__produces_expected():
    crab_posns = [16,1,2,0,4,2,7,1,2,14]
    expected_fuel = 37
    result_fuel = pesky_whales.least_fuel_required(crab_posns, increase_burn_rate=False)
    assert result_fuel == expected_fuel


def test__least_fuel_required_increase_burn_rate__their_sample__produces_expected():
    crab_posns = [16,1,2,0,4,2,7,1,2,14]
    expected_fuel = 168
    result_fuel = pesky_whales.least_fuel_required(crab_posns, increase_burn_rate=True)
    assert result_fuel == expected_fuel


FunctionInput = namedtuple("function_input", "from_pos to_pos expected_fuel")


@pytest.mark.parametrize("from_pos, to_pos, expected_fuel", [
    FunctionInput(from_pos=0, to_pos=5, expected_fuel=15),
    FunctionInput(from_pos=4, to_pos=5, expected_fuel=1),
    FunctionInput(from_pos=16, to_pos=5, expected_fuel=66),
], ids=["from 0 to 5", "from 4 to 5", "from 16 to 5"])
def test__how_much_fuel(from_pos, to_pos, expected_fuel):
    result_fuel = pesky_whales.how_much_fuel(from_pos, to_pos, increase_burn_rate=True)
    assert result_fuel == expected_fuel

