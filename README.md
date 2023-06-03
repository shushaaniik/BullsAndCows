# BullsAndCows

Welcome to Bulls and Cows, a versatile code-breaking game implementation designed to provide a thrilling experience for players of all levels. Whether you prefer challenging the computer, testing your deduction skills, or simulating a teaching scenario, this project offers various modes to suit your gameplay preferences.

## Introduction
Bulls and Cows is a classic game where one player creates a secret code, and the other player attempts to crack it through a series of guesses. In this project, I have expanded upon the traditional rules to bring you a comprehensive Bulls and Cows experience.

## Modes

- ### Computer Guessing Mode
    Are you up for the challenge? In Computer Guessing Mode, you get to create the secret code, and the computer will do its best to crack it. Test your skills as you try to stump the computer with your cunning code-making abilities. Can you create an unbreakable code?

- ### User Guessing Mode
    In User Guessing Mode, the computer generates a secret code, and your challenge is to guess the code. Utilize your code-breaking skills and deductive reasoning to make guesses and crack the computer's hidden combination. Can you outwit the computer and successfully decipher the secret code it has created? Test your abilities and strive for victory in this exciting mode.

- ### Computer-User Guessing Mode
    In Computer-User Guessing Mode, you and the computer engage in a head-to-head code-breaking battle. The computer selects a secret code, and your task is to make guesses and crack the code before the computer can decipher your secret combination. Strategize, make calculated moves, and use your code-breaking skills to outsmart the computer.

- ### Computer Teaching Simulation Mode
    In the Computer Teaching Simulation Mode, you can observe the computer acting as a teacher to help you improve your code-breaking skills. The computer will guide you through the process, providing tips.

## Customizable Code Length
My implementation allows you to play with secret codes of any length between 1 and 9 digits. Whether you prefer a quick and straightforward challenge or a complex mind-bending puzzle, you can customize the code length to match your desired level of difficulty.


## Rules

1. The code-maker generates a secret code consisting of a sequence of unique digits (e.g., "5372").

2. The code-breaker makes guesses by providing sequences of digits, attempting to crack the secret code.

3. After each guess, the code-maker provides feedback in the form of "bulls" and "cows".

- A "bull" represents a correct digit in the correct position.

- A "cow" represents a correct digit in the wrong position.

4. The code-breaker uses the feedback to make informed guesses and narrows down the possible combinations.

5. The guessing process continues until the code-breaker correctly guesses the secret code, or the maximum allowed attempts are reached.

6. The code-maker wins if the code-breaker fails to guess the secret code within the given attempts.

## Usage:

```
git clone https://github.com/shushaaniik/BullsAndCows.git
cd BullsAndCows
./scripts/install_requirements.sh
python3 src/main.py
```

Pay attention to the instructions provided by the program as you progress through the game.


## Tests

This project includes a comprehensive suite of unit tests to ensure the accuracy. The unit tests cover various functionalities and edge cases, verifying that the game logic functions as intended.


**Enjoy playing Bulls and Cows in the mode of your choice, challenge yourself, and have fun!**
