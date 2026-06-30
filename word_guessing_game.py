import random as rd

words = ['mango',"apple","graphs","orange","banana"]
print("Guess the Word from {}".format(words))

guess = 0

while True:
    word = rd.choice(words)
    user_input_word = input("Enter a word: ")
    guess += 1

    if (user_input_word not in words):
        print("your word not in the words list.")

    if (user_input_word == word):
        print("congrats you guessed correct word.")
        break
    else:
        print("Sorry Wrong Guessing Try Again!")
        continue

print('your total guesses:',guess)