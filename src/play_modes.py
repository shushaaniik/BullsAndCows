from src.utils.play_modes_utils import *


class PlayMode:
    def __init__(self, length: int):
        self.__length = length

    def user_guessing_mode(self) -> None:
        computer_code: str = generate_random_code(self.__length)
        attempts: int = 0
        while True:
            attempts += 1
            response: str = get_guess(attempts)
            bulls, cows = get_bulls_cows(response, computer_code, self.__length)

            if is_right_guess(bulls, cows, self.__length):
                print(f"That's right! The code was {response}")
                break
            elif is_invalid_guess(bulls, cows):
                print(f"That's a bad guess! Try again")
                attempts -= 1
                continue
            else:
                print(f"Bulls: {bulls}, Cows: {cows}")

    def computer_guessing_mode(self) -> None:
        possible_codes: List[str] = generate_all_codes(self.__length)
        guess: str = possible_codes[0]
        attempts: int = 1
        while True:
            display_guess(attempts, guess)
            bulls, cows = get_response_bulls_and_cows()
            if not is_valid_bulls_and_cows(bulls, cows, self.__length):
                print("Impossible! Check again.")
                continue
            possible_codes = eliminate_impossible_codes(guess, possible_codes,
                                                        int(bulls), int(cows), self.__length)
            if is_the_only_possible_code(possible_codes):
                print(f"The correct code is {possible_codes[0]}")
                break
            if not are_valid_responses(possible_codes):
                print(f"You've got mistake somewhere. Let's play again.")
                break
            guess = possible_codes[0]
            attempts += 1

    def computer_user_mode(self):
        computer_code = generate_random_code(self.__length)
        possible_codes = generate_all_codes(self.__length)
        guess = possible_codes[0]
        attempts = 0
        while True:
            attempts += 1
            # computer
            display_computers_guess(attempts, guess)
            bulls, cows = get_response_bulls_and_cows()
            possible_codes = eliminate_impossible_codes(guess, possible_codes,
                                                        int(bulls), int(cows), self.__length)
            if is_the_only_possible_code(possible_codes):
                print(f"The correct code is {possible_codes[0]}")
                print("Computer wins!")
                break
            guess = possible_codes[0]

            # user
            user_guess = get_guess(attempts)
            bulls, cows = get_bulls_cows(user_guess, computer_code, self.__length)
            if is_right_guess(bulls, cows, self.__length):
                print(f"That's right! The code was {user_guess}")
                break
            elif is_invalid_guess(bulls, cows):
                print(f"That's an invalid guess! Try again")
                attempts -= 1
                continue
            else:
                print(f"Bulls: {bulls}, Cows: {cows}")

    def computer_teaching_simulation(self):
        computer_code: str = generate_random_code(self.__length)
        possible_codes: List[str] = generate_all_codes(self.__length)
        attempts = 1
        while True:
            response: str = get_guess(attempts)
            bulls, cows = get_bulls_cows(response, computer_code, self.__length)
            if not are_valid_responses(possible_codes):
                print(f"You've got mistake somewhere. Let's play again.")
                break
            if is_right_guess(bulls, cows, self.__length):
                print(f"That's right! The code was {response}")
                break
            elif is_invalid_guess(bulls, cows):
                print(f"That's an invalid guess! Try again")
                attempts -= 1
                continue
            elif response not in possible_codes:
                print(f"That's a really bad guess. Try {possible_codes[0]}")
                continue
            else:
                print(f"Bulls: {bulls}, Cows: {cows}")
            possible_codes = eliminate_impossible_codes(response, possible_codes,
                                                        bulls, cows, self.__length)
            attempts += 1
