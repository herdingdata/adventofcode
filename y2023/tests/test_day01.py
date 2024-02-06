from y2023.day01 import trebuchet_calibration


def test__pt1__sample1():
    txtin = "1abc2"
    assert trebuchet_calibration.get_calibration_value_pt1(txtin) == 12


def test__pt1__sample2():
    txtin = "pqr3stu8vwx"
    assert trebuchet_calibration.get_calibration_value_pt1(txtin) == 38


def test__pt1__sample3():
    txtin = "a1b2c3d4e5f"
    assert trebuchet_calibration.get_calibration_value_pt1(txtin) == 15


def test__pt1__sample4():
    txtin = "treb7uchet"
    assert trebuchet_calibration.get_calibration_value_pt1(txtin) == 77


# ---------
def test__pt2__sample1():
    txtin = "two1nine"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 29


def test__pt2__sample2():
    txtin = "eightwothree"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 83


def test__pt2__sample3():
    txtin = "abcone2threexyz"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 13


def test__pt2__sample4():
    txtin = "xtwone3four"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 24


def test__pt2__sample5():
    txtin = "4nineeightseven2"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 42


def test__pt2__sample6():
    txtin = "zoneight234"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 14


def test__pt2__sample7():
    txtin = "7pqrstsixteen"
    assert trebuchet_calibration.get_calibration_value_pt2(txtin) == 76








