# Eddited by Nolan Kelley

import random
myNumber = 0

def play():
    x = float(input("Please select a lower bound: "))
    y = float(input("Now select an upper bound: "))
    myNumber = random.randint(x,y)
    print("I have chosen a secret number between " + str(x) + " and " + str(y) + "!")
    guess = float(input("Please now make a guess: "))
    while guess != myNumber:
        if guess > myNumber:
            guess = float(input("My number is lower than that! Try again: "))
        else:
            guess = float(input("My number is higher than that! Try again: "))
    print("Huzzah! You guessed it. The secret number was " + str(myNumber) + ".")
        
play()