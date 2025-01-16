# Question8: Guess the Number Game
# This is a simple game where the user guesses a randomly generated number.
import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Providing feedback based on the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")

# Calling the game function
guess_number_game()
