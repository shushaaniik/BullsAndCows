from play_modes import PlayMode as PM

while True:
    length = int(input("How long do you want your code to be? "))
    if not (length < 1 or length > 10):
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
    if mode == 1:
        play_mode.user_guessing_mode()
        break
    elif mode == 2:
        play_mode.computer_guessing_mode()
        break
    elif mode == 3:
        play_mode.computer_user_mode()
        break
    elif mode == 4:
        play_mode.computer_teaching_simulation()
        break
    else:
        print("Invalid mode:( Try again.")
