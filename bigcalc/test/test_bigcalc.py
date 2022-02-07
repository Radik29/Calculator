import pytest
from ..src.bigcalc import main, ArgumentError


class TestBigCalc:
    def test_not_enough_arguments(self):
        argv = ["bigcalc"]

        with pytest.raises(ArgumentError):
            main(argv)

    def test_accepts_multiple_arguments(self):
        argv = ["bigcalc", "2", "+", "2", "*", "2"]
        got = main(argv)
        assert got == 6

    def test_calculate_with_priority(self):
        argv = ["bigcalc", "(2 + 2) * 2"]
        got = main(argv)
        assert got == 8

    def test_unsupported_symbol_error(self):
        argv = ["bigcalc", "a"]

        with pytest.raises(ValueError) as excinfo:
            main(argv)

        assert "Unsupported symbol" in str(excinfo.value)
