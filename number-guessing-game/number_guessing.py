"""Number Guessing Game: guess a secret number from 1 to 100 before you run out of tries."""

import random

GUESSES_BY_DIFFICULTY = {"easy": 10, "hard": 5}


def get_guess():
    """Asks for a guess until the player types a whole number from 1 to 100."""
    while True:
        answer = input("Enter your guess: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= 100:
            return int(answer)
        print("Please enter a whole number from 1 to 100.")


def main():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty level, Easy or Hard: ").strip().lower()
    if difficulty not in GUESSES_BY_DIFFICULTY:
        print("Invalid choice, defaulting to Easy.")
        difficulty = "easy"
    guesses_remaining = GUESSES_BY_DIFFICULTY[difficulty]

    secret_number = random.randint(1, 100)
    print(f"You have {guesses_remaining} guesses. Good luck!")

    while guesses_remaining > 0:
        guess = get_guess()
        guesses_remaining -= 1

        if guess < secret_number:
            print(f"Too low! {guesses_remaining} guesses left.")
        elif guess > secret_number:
            print(f"Too high! {guesses_remaining} guesses left.")
        else:
            print(f"You got it! The number was {secret_number}.")
            break
    else:
        # Runs only if the loop used up every guess without a correct answer (no `break`).
        print(f"Out of guesses! The number was {secret_number}.")


if __name__ == "__main__":
    main()
