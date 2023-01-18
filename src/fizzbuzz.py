from typing import Union


def fizzbuzz(number: int) -> Union[int, str]:
    return 'Buzz' if number % 5 == 0 else 'Fizz' if number % 3 == 0 else number
