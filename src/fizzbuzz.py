from typing import Union


def fizzbuzz(number: int) -> Union[int, str]:
    return number if number % 3 else 'Fizz'
