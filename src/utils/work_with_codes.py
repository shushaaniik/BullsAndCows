import itertools
import random
import re
from typing import List


def check_code(code: str, length: int) -> bool:
    return not (len(code) != length or
                not re.match("^[0-9]+$", code) or
                len(set(code)) != len(code))


def get_bulls_cows(guess: str, code: str, length: int) -> (int, int):
    if not check_code(guess, length):
        return -1, -1
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if digit == code[i]:
            bulls += 1
        elif digit in code:
            cows += 1
    return bulls, cows


def is_valid_bulls_and_cows(bulls: int, cows: int, length: int) -> bool:
    return not int(bulls) + int(cows) > length


def are_valid_responses(possible_codes: List[str]) -> bool:
    return len(possible_codes) != 0


def eliminate_impossible_codes(guess: str, possible_codes: List[str],
                               bulls: int, cows: int, length: int) -> List[str]:
    new_possible_codes: List[str] = []
    for code in possible_codes:
        if get_bulls_cows(guess, code, length) == (bulls, cows):
            new_possible_codes.append(code)
    return new_possible_codes


def generate_all_codes(length: int) -> List[str]:
    codes: List[str] = []
    for code in itertools.product(range(10), repeat=length):
        if len(set(code)) == length:
            codes.append(''.join(str(d) for d in code))
    return codes


def generate_random_code(length: int) -> str:
    digits = list(range(10))
    random_code = ''.join(str(d) for d in random.sample(digits, length))
    return random_code


def is_valid_length(length: int) -> bool:
    return not (length < 1 or length > 10)
