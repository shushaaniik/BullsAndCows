from utils.work_with_codes import get_bulls_cows,\
                                  generate_all_codes,\
                                  eliminate_impossible_codes,\
                                  generate_random_code


class PlayMode:
    def __init__(self, length: int):
        self.__length = length

    def user_guessing_mode(self):
        computer_code = generate_random_code(self.__length)
        attempts = 0
        while True:
            attempts += 1
            response = input(f"Enter your guess #{attempts}: ")
            bulls, cows = get_bulls_cows(response, computer_code, self.__length)
            if bulls == self.__length and cows == 0:
                print(f"That's right! The code was {response}")
                break
            else:
                print(f"Bulls: {bulls}, Cows: {cows}")

    def computer_guessing_mode(self):
        possible_codes = generate_all_codes(self.__length)
        guess = possible_codes[0]
        attempts = 1
        while True:
            print(f"Guess #{attempts}: {guess}")
            response = input("Enter the number of bulls and cows, separated by a space: ")
            bulls, cows = response.split()
            if int(bulls) + int(cows) > self.__length:
                print("Impossible! Check again.")
                continue
            possible_codes = eliminate_impossible_codes(guess, possible_codes,
                                                        int(bulls), int(cows), self.__length)
            if len(possible_codes) == 1:
                print(f"The correct code is {possible_codes[0]}")
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
            print(f"Computer's guess #{attempts}: {guess}")
            response = input("Enter the number of bulls and cows, separated by a space: ")
            bulls, cows = response.split()
            possible_codes = eliminate_impossible_codes(guess, possible_codes,
                                                        int(bulls), int(cows), self.__length)
            if len(possible_codes) == 1:
                print(f"The correct code is {possible_codes[0]}")
                print("Computer wins!")
                break
            guess = possible_codes[0]

            # user
            user_guess = input(f"Enter your guess #{attempts}: ")
            bulls, cows = get_bulls_cows(user_guess, computer_code, self.__length)
            if bulls == 4 and cows == 0:
                print(f"That's right! The code was {user_guess}")
                print("User wins!")
                break
            else:
                print(f"Bulls: {bulls}, Cows: {cows}")
