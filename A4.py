import random

def guessing_game():
    attempts = 0
    number = random.randint(1, 100)

    print("Welcome to the number guessing game! Make a guess between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("NaN")

guessing_game()