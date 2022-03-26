"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    square_number = [number ** 2 for number in args]
    return square_number


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    flag = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            flag = False
            break
        d += 1
    if flag:
        return True
    else:
        return False

def filter_numbers(numbers, refund):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if refund == 'odd':
        result = [num for num in numbers if num % 2 != 0]
    elif refund == 'even':
        result = [num for num in numbers if num % 2 == 0]
    else:
        result = list(filter(is_prime, numbers))
    return result
