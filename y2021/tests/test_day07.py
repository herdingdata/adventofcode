from y2021.day07 import pesky_whales


def test__least_fuel_required__their_sample__produces_expected():
    crab_posns = [16,1,2,0,4,2,7,1,2,14]
    expected_fuel = 37
    result_fuel = pesky_whales.least_fuel_required(crab_posns)
    assert result_fuel == expected_fuel


def test__least_fuel_required_increase_burn_rate__their_sample__produces_expected():
    crab_posns = [16,1,2,0,4,2,7,1,2,14]
    expected_fuel = 168
    result_fuel = pesky_whales.least_fuel_required_increase_burn_rate(crab_posns)
    assert result_fuel == expected_fuel


def test__how_much_fuel__from_0_to_5():
    from_pos = 0
    to_pos = 5
    expected_fuel = 15
    result_fuel = pesky_whales.how_much_fuel(from_pos, to_pos)
    assert result_fuel == expected_fuel


def test__how_much_fuel__from_4_to_5():
    from_pos = 4
    to_pos = 5
    expected_fuel = 1
    result_fuel = pesky_whales.how_much_fuel(from_pos, to_pos)
    assert result_fuel == expected_fuel


def test__how_much_fuel__from_16_to_5():
    from_pos = 16
    to_pos = 5
    expected_fuel = 66
    result_fuel = pesky_whales.how_much_fuel(from_pos, to_pos)
    assert result_fuel == expected_fuel
