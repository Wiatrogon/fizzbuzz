import pytest

from src.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [3, 6, 9])
def test_fizzbuzz_returns_fizz_when_divisible_only_by_3(number):
    assert fizzbuzz(number) == 'Fizz'


@pytest.mark.parametrize("number", [5, 10, 20])
def test_fizzbuzz_returns_buzz_when_divisible_only_by_5(number):
    assert fizzbuzz(number) == 'Buzz'
