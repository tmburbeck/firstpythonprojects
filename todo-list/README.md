# To-Do List

A menu-driven to-do list that runs in the terminal. Tasks are kept in memory while the program runs.

## Run it

```bash
python todo_list.py
```

## Example

```
--- TO-DO LIST ---
1. Add a task
2. View tasks
3. Mark a task as done
4. Remove a task
5. Exit
Enter a choice: 1
Enter a task: Buy milk
Added: Buy milk
Enter a choice: 2

Your tasks:
1. Buy milk - Not done
```

## What I practiced

- Storing records as a list of dictionaries
- Numbering items for display with `enumerate(..., start=1)`
- Converting between the numbers people see (from 1) and list positions (from 0)
- Mapping menu choices to functions with a dictionary
- Sharing code between features with a helper function (`choose_task`)
