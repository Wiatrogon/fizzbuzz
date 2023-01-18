import pytest

from src.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [3, 6, 9])
def test_should_return_fizz_when_divisible_only_by_3(number):
    assert fizzbuzz(number) == 'Fizz'


@pytest.mark.parametrize("number", [5, 10, 20])
def test_should_return_buzz_when_divisible_only_by_5(number):
    assert fizzbuzz(number) == 'Buzz'


@pytest.mark.parametrize("number", [1, 2, 4, 7, 8, 11])
def test_should_return_number_when_not_divisible_by_3_or_5(number):
    assert fizzbuzz(number) == number


@pytest.mark.parametrize("number", [0, 15, 30, 60, 120])
def test_should_return_fizzbuzz_when_divisible_both_by_3_and_5(number):
    assert fizzbuzz(number) == 'FizzBuzz'
