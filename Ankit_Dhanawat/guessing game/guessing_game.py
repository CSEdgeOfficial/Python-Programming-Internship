import random
   
def genareted_number():
    
    genareted_number=random.randint(1, 100)
    
    
    print("Welcome to the Guessing Game!")
    print("You heve maximum 10 chance.")
    
    for attempts in range (0, 10):
        user_choice = int(input("Enter your number in 1 to 100 : "))
        attempts += 1
        
        if user_choice < genareted_number:
            print("Too low! Try again.")
        elif user_choice>genareted_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number in", attempts, "attempts.")
            break
    else:    
        print("Sorry, you've run out of attempts. The number was", genareted_number)

genareted_number()