import pytest
from ..src.bigcalc import main


class TestDiv:
    def test_two_integers(self):
        argv = ["bigcalc", "6 / 3"]
        got = main(argv)
        assert got == 2

    def test_two_integers_with_round(self):
        argv = ["bigcalc", "5 / 2"]
        got = main(argv)
        assert got == 2

    def test_with_negative_argument(self):
        argv = ["bigcalc", "-4 / 2"]
        got = main(argv)
        assert got == -2

    def test_two_big_integers(self):
        argv = ["bigcalc", "340282366920938463463374607431768211456 / 18446744073709551616"]
        got = main(argv)
        assert got == 18446744073709551616

    def test_division_by_zero_error(self):
        argv = ["bigcalc", "1 / 0"]

        with pytest.raises(ZeroDivisionError):
            main(argv)
