from play_modes import PlayMode as PM
from tkinter import *
from tkinter import font


def create_entry_handler(entry):
    def on_enter_pressed(event):
        text = entry.get()

    return on_enter_pressed


def start():
    start_button.place_forget()

    get_length_text = "How long do you want your code to be? "
    get_length_label = Label(window, text=get_length_text, font=font.Font(size=13))
    get_length_label.place(x=30, y=20)

    global code_length
    entry = Entry(window)
    entry.place(x=450, y=20)
    handler = create_entry_handler(entry)
    entry.bind("<Return>", handler)
    code_length = str(entry.get())
    if code_length >= '1' or code_length <= '9':

    print(code_length)


window = Tk()
window.geometry("960x540")

image = PhotoImage(file="../UI/resources/backgrounds/background_1.png").subsample(2, 2)
background_label = Label(window, image=image)
background_label.place(x=0, y=0)

start_button = Button(window, command=start, text='Start')
start_button.configure(width=10, height=3)
start_button.place(x=30, y=20)

quit_button = Button(window, command=quit, text='Quit')
quit_button.place(x=850, y=20)

code_length = ''

window.mainloop()

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

mode = int(input("Pick a mode to play! "))
if mode == 1:
    play_mode.user_guessing_mode()
elif mode == 2:
    play_mode.computer_guessing_mode()
elif mode == 3:
    play_mode.computer_user_mode()
elif mode == 4:
    play_mode.computer_teaching_simulation()
else:
    print("Invalid mode:( Try again.")
