import pytest
from ..src.bigcalc import main


class TestFactorial:
    def test_two_integers(self):
        argv = ["bigcalc", "5!"]
        got = main(argv)
        assert got == 120

    def test_two_big_integers(self):
        argv = ["bigcalc", "20!"]
        got = main(argv)
        assert got == 2432902008176640000

    def test_incorrect_usage_error(self):
        argv = ["bigcalc", "(2)!"]

        with pytest.raises(ValueError) as excinfo:
            main(argv)

        assert "Factorial operator must be used with numbers only" in str(excinfo.value)
