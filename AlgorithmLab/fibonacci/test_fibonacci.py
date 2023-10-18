from fibonacci import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(4) == 3
    assert fib(8) == 21
    assert fib(15) == 610
