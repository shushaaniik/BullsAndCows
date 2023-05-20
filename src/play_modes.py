from utils.work_with_codes import get_bulls_cows,\
                                  generate_all_codes,\
                                  eliminate_impossible_codes,\
                                  generate_random_code


def user_guessing_mode():
    computer_code = generate_random_code()
    attempts = 0
    while True:
        attempts += 1
        response = input(f"Enter your guess #{attempts}: ")
        bulls, cows = get_bulls_cows(response, computer_code)
        if bulls == 4 and cows == 0:
            print(f"That's right! The code was {response}")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")


def computer_guessing_mode():
    possible_codes = generate_all_codes()
    guess = possible_codes[0]
    attempts = 1
    while True:
        print(f"Guess #{attempts}: {guess}")
        response = input("Enter the number of bulls and cows, separated by a space: ")
        bulls, cows = response.split()
        if int(bulls) + int(cows) > 4:
            print("Impossible! Check again.")
            continue
        bulls = int(bulls)
        cows = int(cows)
        possible_codes = eliminate_impossible_codes(guess, possible_codes, bulls, cows)
        if len(possible_codes) == 1:
            print(f"The correct code is {possible_codes[0]}")
            break
        guess = possible_codes[0]
        attempts += 1


def computer_user_mode():
    computer_code = generate_random_code()
    possible_codes = generate_all_codes()
    guess = possible_codes[0]
    attempts = 0
    while True:
        attempts += 1
        # computer
        print(f"Computer's guess #{attempts}: {guess}")
        response = input("Enter the number of bulls and cows, separated by a space: ")
        bulls, cows = response.split()
        bulls = int(bulls)
        cows = int(cows)
        possible_codes = eliminate_impossible_codes(guess, possible_codes, bulls, cows)
        if len(possible_codes) == 1:
            print(f"The correct code is {possible_codes[0]}")
            print("Computer wins!")
            break
        guess = possible_codes[0]

        # user
        user_guess = input(f"Enter your guess #{attempts}: ")
        bulls, cows = get_bulls_cows(user_guess, computer_code)
        if bulls == 4 and cows == 0:
            print(f"That's right! The code was {user_guess}")
            print("User wins!")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")


