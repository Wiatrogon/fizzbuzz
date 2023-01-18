from typing import Union


def fizzbuzz(number: int) -> Union[int, str]:
    if number % 3 == 0:
        if number % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'

    return number
