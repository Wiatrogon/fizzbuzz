import pytest

from src.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [0, 3, 6, 9])
def test_fizzbuzz_returns_fizz_when_divisible_only_by_3(number):
    assert fizzbuzz(number) == 'Fizz'
