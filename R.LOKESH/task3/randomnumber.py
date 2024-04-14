import random

chance=0
score=100 
number=random.randint(1,100)
print(number)
print("guessing number game you have 10 chances guess the number")
while chance<10:
    guess=int(input("Enter any number:"))
    if guess==number:
        print("you guessed correct !!")
        score+=10
        break
    else:
        print("You are wrong retry")
        score-=10
    chance+=1
    print("your score is",score)
print("your final score:",score)
