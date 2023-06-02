from utils.work_with_codes import *


def get_guess(attempts: int) -> str:
    return input(f"Enter your guess #{attempts}: ")


def display_guess(attempts: int, guess: str) -> None:
    print(f"Guess #{attempts}: {guess}")


def display_computers_guess(attempts: int, guess: str) -> None:
    print(f"Computer's guess #{attempts}: {guess}")


def is_right_guess(bulls: int, cows: int, length: int) -> bool:
    return (bulls, cows) == (length, 0)


def is_invalid_guess(bulls: int, cows: int) -> bool:
    return (bulls, cows) == (-1, -1)


def is_the_only_possible_code(possible_codes: List[str]) -> bool:
    return len(possible_codes) == 1


def get_response_bulls_and_cows() -> (int, int):
    response: str = input("Enter the number of bulls and cows, separated by a space: ")
    found_space = response.find(' ')
    if found_space == -1:
        print(f"Invalid bulls and cows!")
    return response.split()


def is_user_guessing_mode(mode: int) -> bool:
    return mode == 1


def is_computer_guessing_mode(mode: int) -> bool:
    return mode == 2


def is_computer_user_mode(mode: int) -> bool:
    return mode == 3


def is_computer_teaching_simulation(mode: int) -> bool:
    return mode == 4
