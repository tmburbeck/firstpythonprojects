# Number Guessing Game

The computer picks a secret number from 1 to 100. Choose **Easy** (10 guesses) or **Hard** (5 guesses), and after each guess you're told whether to go higher or lower.

## Run it

```bash
python number_guessing.py
```

## Example

```
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
Choose a difficulty level, Easy or Hard: hard
You have 5 guesses. Good luck!
Enter your guess: 50
Too high! 4 guesses left.
Enter your guess: 25
Too low! 3 guesses left.
Enter your guess: 37
You got it! The number was 37.
```

## What I practiced

- Generating random numbers with `random.randint`
- Looping with `while`, and using `while ... else` to detect running out of guesses
- Validating input so a typo asks again instead of crashing
- Looking up settings (guesses per difficulty) in a dictionary
