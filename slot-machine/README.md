# Slot Machine

A text-based slot machine. Deposit some money, choose how many lines to bet on (1 to 3) and how much per line, then spin a 3×3 reel. A line pays out when all three symbols on it match; rarer symbols pay more.

| Symbol | Copies per reel | Payout (× bet) |
|---|---|---|
| A | 2 | 5 |
| B | 4 | 4 |
| C | 6 | 3 |
| D | 8 | 2 |

## Run it

```bash
python slot_machine.py
```

## Example

```
Enter amount to deposit: $50
Current balance is $50
Press Enter to play (q to quit).
Enter number of lines to bet on (1-3): 1
Enter amount to bet on each line: $10
You are betting $10 on 1 lines. Total bet is $10.
C | C | C
B | D | A
D | B | C
You won $30!
You won on lines: 1
Current balance is $70
```

## What I practiced

- Breaking a program into small functions, each with one job
- Using dictionaries for game settings (symbol counts and payouts)
- Nested loops, and `for ... else` to check whether every symbol on a line matches
- Random draws without replacement, by removing each drawn symbol from a copy of the reel
- Keeping a running balance across rounds
