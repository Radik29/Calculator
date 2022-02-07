import sys
import re
from .calculate import calculate


class ArgumentError(Exception):
    pass


def help():
    print("Usage:")
    print("\t./bigcalc '<math_expression>'\n")
    print(
        "<math_expressin> -- math formula to calculate. "
        "Supports integer operands, the size can be larger than 64bit. "
    )
    print("Supported operators:")
    print("  x+y -- addition x and y")
    print("  x-y -- substraction y from x")
    print("  x*y -- multiplication x and y")
    print("  x/y -- division of x by y")
    print("  x**y -- raises x to the power y")
    print("  x! -- factorial x")


def join_math(parts):
    return " ".join(parts)


def validate(s):
    valid_symb_re = re.compile(r"^[0-9+\-\*\/!\(\) ]+$")

    if not valid_symb_re.match(s):
        raise ValueError("Unsupported symbol in math expression")


def main(argv):
    if len(argv) < 2:
        help()
        raise ArgumentError()

    math_expr = join_math(argv[1:])

    validate(math_expr)

    return calculate(math_expr)


if __name__ == "__main__":
    try:
        res = main(sys.argv)
    except ArgumentError:
        exit(-1)
    except Exception as e:
        print(e)
        exit(-1)

    print(res)
