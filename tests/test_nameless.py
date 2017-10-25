
from nameless import longest
from nameless.cli import main


def test_main():
    assert main([]) == 0


def test_longest():
    assert longest(['a', 'bc', 'abc']) == 'abc'
