print("Hello! What is your name?")
name = input()

import random

x = random.randint(1, 20)

print(f"Well, {name}, I am thinking of a number between 1 and 20")
print("Take a guess")

guess = int(input())

count = 0

while guess != x:
    if guess < x:
        print("Your guess is too low")
    elif guess > x:
        print("Your guess is too high")
    
    print("Take a guess")
    guess = int(input())
    count += 1

print(f"Good job, {name}! You guessed my number in {count + 1} guesses!")
