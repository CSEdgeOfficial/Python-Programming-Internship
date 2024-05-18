import random
def random_number():
    x=random.randint(1,100)
    print(f"The computer generated number is{x}")
    print("computer choose a number!!!")
    print("ARE YOU READY TO GUESS THE NUMBER!!")
    max=4
    min=0
    print("let's start the game")
    print(f"choose a number between (1 to100)\n NOTE:you will have {max} attempts to guess the number")
    while min<max :
        guess=int(input("enter the number:"))
        min=min+1
        if guess<x:
            print(f"The value you guessed is less than the computer generated number, you lost {min} chances,Try again!!")
        elif guess>x:
            print(f"The value is greater than the computer generated number you lost {min} chances,Try again!!")
        else:
            print("congrats you guessed the number correctly!!")
            print(f"You took {min} attempts")
            return
    print("You've run out of attempts!") 
random_number()
        