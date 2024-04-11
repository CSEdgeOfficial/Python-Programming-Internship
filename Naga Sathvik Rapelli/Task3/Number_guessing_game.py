import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the secret number between 1 and 50. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

def main():
    number_guessing_game()

if __name__ == "__main__":
    main()
