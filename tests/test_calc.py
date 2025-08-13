def test_calc(calc_t):
    result = calc_t.calculate_price()
    assert result == 7500


def test_calc2(calc_t2):
    result = calc_t2.calculate_price()
    assert result == 78750
