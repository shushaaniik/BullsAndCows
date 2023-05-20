from play_modes import user_guessing_mode, computer_guessing_mode, computer_user_mode


print("1. User guessing mode.\n2. Computer guessing mode.\n"
      "3. User-Computer mode.")
mode = int(input("Pick a mode to play! "))
if mode == 1:
    user_guessing_mode()
elif mode == 2:
    computer_guessing_mode()
elif mode == 3:
    computer_user_mode()
else:
    print("Invalid mode:)")
