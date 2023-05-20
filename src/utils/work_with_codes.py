import itertools
import random
import re


def check_code(code: str, length: int):
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


def eliminate_impossible_codes(guess, possible_codes, bulls, cows, length):
    new_possible_codes = []
    for code in possible_codes:
        if get_bulls_cows(guess, code, length) == (bulls, cows):
            new_possible_codes.append(code)
    return new_possible_codes


def generate_all_codes(length):
    codes = []
    for code in itertools.product(range(10), repeat=length):
        if len(set(code)) == length:
            codes.append(''.join(str(d) for d in code))
    return codes


def generate_random_code(length):
    digits = list(range(10))
    random_code = ''.join(str(d) for d in random.sample(digits, length))
    return random_code
