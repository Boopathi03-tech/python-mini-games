<<<<<<< HEAD
import random as rd

low = 1
high = 100

guess = 0

number = rd.randint(low,high)

while True:
    guessing = int(input(f"Enter number from {low} to {high}:"))
    guess += 1

    if guessing > number:
        print("guessed number is too high.")
    elif guessing < number:  
        print("guessed number is too low.")
    else:
        print(f"{number} is correct.")
        break
    
print("You Guessed correct number.")
=======
import random as rd

low = 1
high = 100

guess = 0

number = rd.randint(low,high)

while True:
    guessing = int(input(f"Enter number from {low} to {high}:"))
    guess += 1

    if guessing > number:
        print("guessed number is too high.")
    elif guessing < number:  
        print("guessed number is too low.")
    else:
        print(f"{number} is correct.")
        break
    
print("You Guessed correct number.")
>>>>>>> a8048eda26c11c1a53fa12ced50765f6036c28b9
print("your total guesses is",guess)