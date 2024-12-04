import random

def number_guessing_game():
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()