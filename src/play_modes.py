from utils.play_modes_utils import *
from abc import ABC
from enum import Enum
from typing import List


class Mode(Enum):
    USER_GUESSING: int = 1
    COMPUTER_GUESSING: int = 2
    COMPUTER_USER_GUESSING: int = 3
    COMPUTER_TEACHING_SIMULATION: int = 4


class State(Enum):
    Default: int = 0
    RIGHT_CODE: int = 1
    BAD_GUESS: int = 2
    GET_BULLS_COWS: int = 3
    INVALID_BULLS_COWS: int = 4
    GUESSED_CODE: int = 5
    INVALID_RESPONSES: int = 6


class PlayMode(ABC):
    __state: int = State.Default.value
    __length: int = 0

    def __init__(self, length: int):
        self.__length = length

    def get_length(self) -> int:
        return self.__length

    def get_state(self) -> int:
        return self.__state

    def update(self, state: int) -> None:
        self.__state = state

    def refresh(self, code: str='', bulls: int=0, cows: int=0):
        if self.__state == State.RIGHT_CODE.value:
            print(f"That's right! The code was {code}")
        elif self.__state == State.BAD_GUESS.value:
            print(f"That's a bad guess! Try again")
        elif self.__state == State.GET_BULLS_COWS.value:
            print(f"Bulls: {bulls}, Cows: {cows}")
        elif self.__state == State.INVALID_BULLS_COWS.value:
            print("Impossible! Check again.")
        elif self.__state == State.GUESSED_CODE.value:
            print(f"The correct code is {code}")
        elif self.__state == State.INVALID_RESPONSES:
            print(f"You've got mistake somewhere. Let's play again.")


    def __init__(self, length) -> None:
        self.__length = length

    def run(self) -> None:
        pass


class UserGuessingMode(PlayMode):
    def user_guessing(self, attempts: int, computer_code: str) -> None:
        response: str = get_guess(attempts)
        bulls, cows = get_bulls_cows(response, computer_code, self.get_length())

        if is_right_guess(bulls, cows, self.get_length()):
            self.update(State.RIGHT_CODE.value)
            self.refresh(response)

        elif is_invalid_guess(bulls, cows):
            self.update(State.BAD_GUESS.value)
            self.refresh()
            attempts -= 1
        else:
            self.update(State.GET_BULLS_COWS.value)
            self.refresh('', bulls, cows)

    def run(self) -> None:
        computer_code: str = generate_random_code(self.get_length())
        attempts: int = 0
        while self.get_state() != State.RIGHT_CODE.value:
            attempts += 1
            self.user_guessing(attempts, computer_code)


class ComputerGuessingMode(PlayMode):
    def computer_guessing(self, attempts: int, possible_codes: List[str]) -> None:
        guess: str = possible_codes[0]
        display_guess(attempts, guess)
        bulls, cows = get_response_bulls_and_cows()
        if not is_valid_bulls_and_cows(int(bulls), int(cows), int(self.get_length())):
            self.update(State.INVALID_BULLS_COWS.value)
            self.refresh()

        possible_codes = eliminate_impossible_codes(guess, possible_codes,
                                                    int(bulls), int(cows), self.get_length())
        if is_the_only_possible_code(possible_codes):
            self.update(State.GUESSED_CODE.value)
            self.refresh(guess)

        if not are_valid_responses(possible_codes):
            self.update(State.INVALID_RESPONSES.value)
            self.refresh()

    def run(self) -> None:
        attempts: int = 1
        possible_codes = generate_all_codes(self.get_length())
        while (not is_the_only_possible_code(possible_codes)) and \
                self.get_state() != State.INVALID_RESPONSES.value:
            self.computer_guessing(attempts, possible_codes)
            attempts += 1


class ComputerUserGuessingMode(PlayMode):
    pass


class ComputerTeachingSimulationMode(PlayMode):
    pass



    # def user_guessing_mode(self) -> None:
    #     computer_code: str = generate_random_code(self.__length)
    #     attempts: int = 0
    #     while True:
    #         attempts += 1
    #         response: str = get_guess(attempts)
    #         bulls, cows = get_bulls_cows(response, computer_code, self.__length)
    #
    #         if is_right_guess(bulls, cows, self.__length):
    #             print(f"That's right! The code was {response}")
    #             break
    #         elif is_invalid_guess(bulls, cows):
    #             print(f"That's a bad guess! Try again")
    #             attempts -= 1
    #             continue
    #         else:
    #             print(f"Bulls: {bulls}, Cows: {cows}")

    # def computer_guessing_mode(self) -> None:
    #     possible_codes: List[str] = generate_all_codes(self.__length)
    #     guess: str = possible_codes[0]
    #     attempts: int = 1
    #     while True:
    #         display_guess(attempts, guess)
    #         bulls, cows = get_response_bulls_and_cows()
    #         if not is_valid_bulls_and_cows(bulls, cows, self.__length):
    #             print("Impossible! Check again.")
    #             continue
    #         possible_codes = eliminate_impossible_codes(guess, possible_codes,
    #                                                     int(bulls), int(cows), self.__length)
    #         if is_the_only_possible_code(possible_codes):
    #             print(f"The correct code is {possible_codes[0]}")
    #             break
    #         if not are_valid_responses(possible_codes):
    #             print(f"You've got mistake somewhere. Let's play again.")
    #             break
    #         guess = possible_codes[0]
    #         attempts += 1
    #
    # def computer_user_mode(self):
    #     computer_code = generate_random_code(self.__length)
    #     possible_codes = generate_all_codes(self.__length)
    #     guess = possible_codes[0]
    #     attempts = 0
    #     while True:
    #         attempts += 1
    #         # computer
    #         display_computers_guess(attempts, guess)
    #         bulls, cows = get_response_bulls_and_cows()
    #         possible_codes = eliminate_impossible_codes(guess, possible_codes,
    #                                                     int(bulls), int(cows), self.__length)
    #         if is_the_only_possible_code(possible_codes):
    #             print(f"The correct code is {possible_codes[0]}")
    #             print("Computer wins!")
    #             break
    #         guess = possible_codes[0]
    #
    #         # user
    #         user_guess = get_guess(attempts)
    #         bulls, cows = get_bulls_cows(user_guess, computer_code, self.__length)
    #         if is_right_guess(bulls, cows, self.__length):
    #             print(f"That's right! The code was {user_guess}")
    #             break
    #         elif is_invalid_guess(bulls, cows):
    #             print(f"That's an invalid guess! Try again")
    #             attempts -= 1
    #             continue
    #         else:
    #             print(f"Bulls: {bulls}, Cows: {cows}")
    #
    # def computer_teaching_simulation(self):
    #     computer_code: str = generate_random_code(self.__length)
    #     possible_codes: List[str] = generate_all_codes(self.__length)
    #     attempts = 1
    #     while True:
    #         response: str = get_guess(attempts)
    #         bulls, cows = get_bulls_cows(response, computer_code, self.__length)
    #         if not are_valid_responses(possible_codes):
    #             print(f"You've got mistake somewhere. Let's play again.")
    #             break
    #         if is_right_guess(bulls, cows, self.__length):
    #             print(f"That's right! The code was {response}")
    #             break
    #         elif is_invalid_guess(bulls, cows):
    #             print(f"That's an invalid guess! Try again")
    #             attempts -= 1
    #             continue
    #         elif response not in possible_codes:
    #             print(f"That's a really bad guess. Try {possible_codes[0]}")
    #             continue
    #         else:
    #             print(f"Bulls: {bulls}, Cows: {cows}")
    #         possible_codes = eliminate_impossible_codes(response, possible_codes,
    #                                                     bulls, cows, self.__length)
    #         attempts += 1


class PlayModeCreation:
    @staticmethod
    def create_play_mode(mode: int, length: int):
        if mode == Mode.USER_GUESSING.value:
            return UserGuessingMode(length)
        elif mode == Mode.COMPUTER_GUESSING.value:
            return ComputerGuessingMode(length)
        elif mode == Mode.COMPUTER_USER_GUESSING.value:
            return ComputerUserGuessingMode(length)
        elif mode == Mode.COMPUTER_TEACHING_SIMULATION.value:
            return ComputerTeachingSimulationMode(length)

