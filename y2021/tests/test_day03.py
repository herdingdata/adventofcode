from y2021.day03 import binary_diagnostic


class TestBinToDec:
    def test__22(self):
        result_decimal = binary_diagnostic.bin_to_dec('10110')
        assert result_decimal == 22

    def test__9(self):
        result_decimal = binary_diagnostic.bin_to_dec('01001')
        assert result_decimal == 9


def test_get_gamma_and_epsilon__their_sample__produces_expected():
    sample_readings = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    expected_gamma =  22
    expected_epsilon = 9

    result_gamma, result_epsilon = binary_diagnostic.get_gamma_and_epsilon(sample_readings)
    assert result_gamma == expected_gamma
    assert result_epsilon == expected_epsilon


def test__o2_generator__their_sample__produces_expected():
    sample_readings = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    expected_o2_generator =  23

    result_o2_gen = binary_diagnostic.get_o2_generator(sample_readings)
    assert result_o2_gen == expected_o2_generator


def test__get_co2_scrubber__their_sample__produces_expected():
    sample_readings = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    expected_co2_scrubber = 10

    result_co2_scrub = binary_diagnostic.get_co2_scrubber(sample_readings)
    assert result_co2_scrub == expected_co2_scrubber


def test__get_life_support_rating__their_sample__produces_expected():
    sample_readings = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    expected_life_support = 230

    result_life_support = binary_diagnostic.get_life_support_rating(sample_readings)
    assert result_life_support == expected_life_support

