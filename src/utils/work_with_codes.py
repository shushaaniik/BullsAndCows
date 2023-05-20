import itertools
import random


def get_bulls_cows(guess, code):
    bulls = 0
    cows = 0
    for i, digit in enumerate(guess):
        if digit == code[i]:
            bulls += 1
        elif digit in code:
            cows += 1
    return bulls, cows


def eliminate_impossible_codes(guess, possible_codes, bulls, cows):
    new_possible_codes = []
    for code in possible_codes:
        if get_bulls_cows(guess, code) == (bulls, cows):
            new_possible_codes.append(code)
    return new_possible_codes


def generate_all_codes():
    codes = []
    for code in itertools.product(range(10), repeat=4):
        if len(set(code)) == 4:
            codes.append(''.join(str(d) for d in code))
    return codes

def generate_random_code():
    digits = list(range(10))
    random_code = ''.join(str(d) for d in random.sample(digits, 4))
    return random_code
