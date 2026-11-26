"""Slot Machine: deposit money, bet on 1-3 lines, and spin a 3x3 reel."""

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# How many of each symbol are on a reel. Rarer symbols pay more.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

# The payout multiplier for a full line of each symbol.
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    """Returns the total winnings and which lines won (a line wins when all its symbols match)."""
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            # The loop finished without a mismatch, so every symbol on this line is the same.
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """Returns a random spin as a list of columns, each holding `rows` symbols."""
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        # Draw from a copy so a symbol can't appear in one column more times than it exists.
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    """Prints the spin row by row, e.g. "A | B | C"."""
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


def deposit():
    """Asks how much money to start with."""
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a whole number greater than 0.")


def get_number_of_lines():
    """Asks how many lines to bet on."""
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print(f"Please enter a number from 1 to {MAX_LINES}.")


def get_bet():
    """Asks how much to bet on each line."""
    while True:
        amount = input("Enter amount to bet on each line: $")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Please enter a whole number from {MIN_BET} to {MAX_BET}.")


def spin(balance):
    """Plays one round and returns how much the balance went up or down."""
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        print(f"You don't have enough money to bet that amount. Your current balance is ${balance}.")

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit). ")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
