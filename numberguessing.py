import random

def number_guessing_game(low, high, max_attempts):
    number_to_guess = random.randint(low, high)
    attempts = 0
    
    print(f"Guess the number between {low} and {high}. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        attempts += 1
        user_guess = input("Enter your guess: ")
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the right number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Try again! You guessed too low.")
        else:
            print("Try again! You guessed too high.")
        
        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
            break

# Start the game
number_guessing_game(1, 100, 10)
