import random

def random_number_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print("The computer has chosen a number!")
    print("ARE YOU READY TO GUESS THE NUMBER!!")

    max_attempts = 4
    attempts = 0

    print("Let's start the game")
    print(f"Choose a number between 1 and 100\nNOTE: You will have {max_attempts} attempts to guess the number")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print(f"The value you guessed is less than the computer generated number. You have used {attempts} out of {max_attempts} attempts. Try again!")
            elif guess > target_number:
                print(f"The value you guessed is greater than the computer generated number. You have used {attempts} out of {max_attempts} attempts. Try again!")
            else:
                print("Congratulations! You guessed the number correctly!")
                print(f"You took {attempts} attempts")
                return
        except ValueError:
            print("Invalid Input: Please enter a valid number.")

    print("You've run out of attempts! The correct number was", target_number)

# Call the function to start the game
random_number_game()
