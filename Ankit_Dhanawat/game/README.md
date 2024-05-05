# Guessing Game Documentation

This is a simple guessing game implemented in Python. The program generates a random number between 1 and 100, and the user has to guess the number within a limited number of attempts.

## Function

### `genareted_number()`

This function generates a random number between 1 and 100 and initiates the guessing game. It prompts the user to guess the number and provides feedback on whether the guess is too low, too high, or correct. It also limits the user to a maximum of 10 attempts.

## Usage

1. Run the script.
2. The program will generate a random number between 1 and 100.
3. You will be prompted to guess the number.
4. Enter your guess within the range of 1 to 100.
5. You will receive feedback on whether your guess is too low, too high, or correct.
6. Continue guessing until you guess the number correctly or exhaust all 10 attempts.

## Example

```
Welcome to the Guessing Game!
You have maximum 10 chances.
Enter your number in 1 to 100 : 50
Too low! Try again.
Enter your number in 1 to 100 : 75
Too high! Try again.
Enter your number in 1 to 100 : 63
Too high! Try again.
Enter your number in 1 to 100 : 58
Too high! Try again.
Enter your number in 1 to 100 : 54
Too low! Try again.
Enter your number in 1 to 100 : 56
Congratulations! You've guessed the number in 6 attempts.
```

## Error Handling

If the user exhausts all 10 attempts without guessing the correct number, the program will display "Sorry, you've run out of attempts. The number was [generated_number]." 