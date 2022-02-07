from ..src.bigcalc import main


class TestPower:
    def test_two_integers(self):
        argv = ["bigcalc", "2**10"]
        got = main(argv)
        assert got == 1024

    def test_with_negative_argument(self):
        argv = ["bigcalc", "-2**10"]
        got = main(argv)
        assert got == -1024

    def test_two_big_integers(self):
        argv = ["bigcalc", "18446744073709551616 ** 2"]
        got = main(argv)
        assert got == 340282366920938463463374607431768211456
