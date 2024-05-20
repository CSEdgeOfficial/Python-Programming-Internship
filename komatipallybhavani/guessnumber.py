import random
n = random.randint(1, 100)python3 guessnumber.py
guess = int(input("Enter an integer from 1 to 100: "))
while True:
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print ("you guessed it right!")
        break
print(f"the computer generated number is {n}")
