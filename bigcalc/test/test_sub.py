from ..src.bigcalc import main


class TestSub:
    def test_two_integers(self):
        argv = ["bigcalc", "4 - 1"]
        got = main(argv)
        assert got == 3

    def test_with_negative_argument(self):
        argv = ["bigcalc", "-2 - 2"]
        got = main(argv)
        assert got == -4

    def test_two_big_integers(self):
        argv = ["bigcalc", "36893488147419103232 - 18446744073709551616"]
        got = main(argv)
        assert got == 18446744073709551616
