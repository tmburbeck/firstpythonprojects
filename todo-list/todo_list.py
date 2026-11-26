# This list holds all tasks. Each task is a dictionary with a 'task' description
# and a 'done' status (True/False). This list persists across all function calls
# because it's defined at the top level, outside any function.
tasks = []


def show_menu():
    # Displays the main menu options to the user every time the loop runs.
    print('\n--- TO-DO LIST ---')
    print('1. Add a task')
    print('2. View task')
    print('3. Mark task as done')
    print('4. Remove task')
    print('5. Exit')


def add_task():
    # Prompts the user for a new task description.
    task = input('Enter a task: ')
    # Adds a new dictionary to the tasks list, starting as not done.
    tasks.append({'task': task, 'done': False})
    print(f'Task added: {task} added!')


def view_task():
    # If the list is empty, let the user know and exit the function early.
    if not tasks:
        print('No tasks added!')
        return

    print('\nYour Tasks:')
    # enumerate() gives both the index and the task itself on each loop.
    # start=1 makes the displayed numbering start at 1 instead of 0,
    # which is more natural for a user-facing list.
    for index, task in enumerate(tasks, start=1):
        # Ternary expression: choose the display text based on the 'done' value.
        status = 'Done!' if task['done'] else 'Not done!'
        print(f'{index}. {task["task"]} - {status}')


def mark_done():
    # Show the current tasks first so the user knows which number to pick.
    view_task()
    if not tasks:
        return  # Nothing to mark done if the list is empty.

    try:
        # Subtract 1 because the user sees 1-based numbering,
        # but list indexing in Python is 0-based.
        index = int(input('Enter a task number to mark done: ')) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done!")
        else:
            print('Invalid task!')
    except ValueError:
        # Catches cases where the user types something that isn't a number.
        print('Please enter a valid number.')


def remove_task():
    # Show the current tasks first so the user knows which number to remove.
    view_task()
    if not tasks:
        return  # Nothing to remove if the list is empty.

    try:
        # Same 1-based to 0-based adjustment as in mark_done().
        index = int(input('Enter a task number to remove: ')) - 1
        if 0 <= index < len(tasks):
            # .pop() removes the item at that index AND returns it,
            # so we can reference what was just removed.
            removed = tasks.pop(index)
            print(f'Removed: {removed["task"]}')
        else:
            print('Invalid task!')
    except ValueError:
        print('Please enter a valid number.')


# Main program loop — keeps showing the menu until the user chooses to exit.
while True:
    show_menu()
    choice = input('Enter a choice: ')

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print('Thank you for your time!')
        break  # Exits the while loop, ending the program.
    else:
        # Catches any input that doesn't match 1-5.
        print('Invalid choice! Try again!')
