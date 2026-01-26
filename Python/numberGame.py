import random
print("Welcome to the Number Guessing Game!. What is your name?")
name = input("Enter your name: ")
print(f"Hello, {name}!, I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guesses in range(1,7):
    print("take a guess.")
    guess = input()
    guess = int(guess)
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess!
if guess == secretNumber:
    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
else:
    print(f"Sorry, the number I was thinking of was {secretNumber}.")   