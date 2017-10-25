
from nameless.cli import main
from nameless import longest


def test_main():
    assert main([]) == 0


def test_longest():
    assert longest(['a', 'bc', 'abc']) == 'abc'
