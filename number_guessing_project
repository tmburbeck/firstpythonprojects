import random

print("Welcome to the Number Guessing Project")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty level. Easy or Hard: \n").strip().lower()

if difficulty == "easy":
    guesses_remaining = 10
elif difficulty == "hard":
    guesses_remaining = 5
else:
    print("Invalid choice, defaulting to Easy.")
    guesses_remaining = 10

secret_number = random.randint(1, 100)
print(f"You have {guesses_remaining} guesses. Good luck!")

while guesses_remaining > 0:
    guess = int(input("Enter your guess: "))
    guesses_remaining -= 1

    if guess < secret_number:
        print(f"Too low! {guesses_remaining} guesses left.")
    elif guess > secret_number:
        print(f"Too high! {guesses_remaining} guesses left.")
    else:
        print(f"You got it! The number was {secret_number}.")
        break
else:
    # This runs if the while loop exhausted all guesses without a `break`
    print(f"Out of guesses! The number was {secret_number}.")
