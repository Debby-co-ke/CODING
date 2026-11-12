# Generate a random number
import random

secret_number = random.randint(1, 100)

while True:
    guess = input("Guess the number between 1 and 100 (or type 'exit' to quit): ")
    
    if guess.lower() == 'exit':
        print("Thanks for playing!")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number:", secret_number)
        break

