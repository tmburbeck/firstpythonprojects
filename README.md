# First Python Projects

The first programs I wrote while learning Python. Each one is a small command-line game or tool, and each lives in its own folder with a README explaining what it does and what it taught me.

| Project | What it does | Python concepts |
|---|---|---|
| [Number Guessing Game](number-guessing-game/) | Guess a secret number from 1 to 100 within 5 or 10 tries | `random`, `while`/`else` loops, input validation |
| [Slot Machine](slot-machine/) | Deposit money, bet on up to 3 lines and spin a 3×3 reel | functions, dictionaries, nested loops, `for`/`else` |
| [To-Do List](todo-list/) | Add, view, complete and remove tasks from a menu | lists of dictionaries, `enumerate`, dispatching menu choices |

## Running a project

Every project uses only the Python standard library, so there is nothing to install. With Python 3 installed:

```bash
git clone https://github.com/tmburbeck/firstpythonprojects.git
cd firstpythonprojects
python number-guessing-game/number_guessing.py
```

Swap in `slot-machine/slot_machine.py` or `todo-list/todo_list.py` to run the others.

## Repository layout

```
firstpythonprojects/
├── number-guessing-game/
│   ├── number_guessing.py
│   └── README.md
├── slot-machine/
│   ├── slot_machine.py
│   └── README.md
├── todo-list/
│   ├── todo_list.py
│   └── README.md
└── README.md
```
