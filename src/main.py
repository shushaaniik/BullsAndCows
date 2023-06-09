from play_modes import PlayMode as PM
from utils.play_modes_utils import *

while True:
    length = int(input("How long do you want your code to be? "))
    if is_valid_length(length):
        break
    else:
        print("Invalid length:( Try again.")

play_mode = PM(length)

print(f"Okay! Get ready to play with {length} digits long codes!")
print("1. User guessing mode.\n"
      "2. Computer guessing mode.\n"
      "3. User-Computer mode.\n"
      "4. Computer teaching mode.")

while True:
    mode = int(input("Pick a mode to play! "))
    if is_user_guessing_mode(mode):
        play_mode.user_guessing_mode()
        break
    elif is_computer_guessing_mode(mode):
        play_mode.computer_guessing_mode()
        break
    elif is_computer_user_mode(mode):
        play_mode.computer_user_mode()
        break
    elif is_computer_teaching_simulation(mode):
        play_mode.computer_teaching_simulation()
        break
    else:
        print("Invalid mode:( Try again.")
