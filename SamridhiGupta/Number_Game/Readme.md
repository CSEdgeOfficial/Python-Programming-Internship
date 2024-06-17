# Random Number Guessing Game

## Overview

This is a simple Python program where the user tries to guess a random number chosen by the computer. The number is between 1 and 100, and the user has a limited number of attempts to guess it correctly.

## Features

- **Random Number Generation**: The program generates a random number between 1 and 100 at the start of each game.
- **User Input**: The user is prompted to enter their guess.
- **Feedback**: The program provides feedback if the guess is too high or too low.
- **Limited Attempts**: The user has up to 4 attempts to guess the number correctly.
- **Victory and Loss Messages**: The program displays a congratulatory message if the user guesses correctly, and a message with the correct number if the user runs out of attempts.

## How to Use

1. **Run the Program**: Execute the script to start the game.
2. **Start Guessing**: Follow the on-screen instructions to enter your guesses.
3. **Receive Feedback**: After each guess, the program will tell you if your guess is too high, too low, or correct.
4. **Win or Lose**: The game ends either when you guess the number correctly or when you run out of attempts.

## Example Usage

```
The computer has chosen a number!
ARE YOU READY TO GUESS THE NUMBER!!
Let's start the game
Choose a number between 1 and 100
NOTE: You will have 4 attempts to guess the number
Enter your guess: 50
The value you guessed is less than the computer generated number. You have used 1 out of 4 attempts. Try again!
Enter your guess: 75
The value you guessed is greater than the computer generated number. You have used 2 out of 4 attempts. Try again!
Enter your guess: 60
The value you guessed is less than the computer generated number. You have used 3 out of 4 attempts. Try again!
Enter your guess: 70
Congratulations! You guessed the number correctly!
You took 4 attempts
```
## Error Handling

The program includes basic error handling to manage common input errors:

1. **Invalid Input**:
    - If the user enters a non-numeric value, the program will display the message: `Invalid Input: Please enter a valid number.`
    - The attempt will not be counted in case of an invalid input.

2. **Out of Attempts**:
    - If the user does not guess the number correctly within the allowed attempts, the program will display the correct number and end the game.
