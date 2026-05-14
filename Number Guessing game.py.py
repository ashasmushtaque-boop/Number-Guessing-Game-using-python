import random

secret=random.randint(1,10)

while True:
    guess=int(input("Enter your number:"))

    if guess == secret:
        print("You are Correct")
        break
    else:
        print("Try Again")
