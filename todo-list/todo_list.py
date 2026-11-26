"""To-Do List: add, view, complete and remove tasks from a simple menu."""

# Every task is a dictionary like {"task": "Buy milk", "done": False}.
tasks = []


def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")


def add_task():
    task = input("Enter a task: ").strip()
    if not task:
        print("A task can't be empty.")
        return
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return

    print("\nYour tasks:")
    # Number the list from 1, since that's how people count.
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{number}. {task['task']} - {status}")


def choose_task(action):
    """Shows the list and asks which task to act on. Returns its position, or None if invalid."""
    view_tasks()
    if not tasks:
        return None

    answer = input(f"Enter the number of the task to {action}: ").strip()
    if answer.isdigit() and 1 <= int(answer) <= len(tasks):
        return int(answer) - 1  # the list starts at 0, the menu numbers start at 1
    print("That isn't a task number on the list.")
    return None


def mark_done():
    index = choose_task("mark as done")
    if index is not None:
        tasks[index]["done"] = True
        print("Marked as done!")


def remove_task():
    index = choose_task("remove")
    if index is not None:
        removed = tasks.pop(index)
        print(f"Removed: {removed['task']}")


def main():
    actions = {"1": add_task, "2": view_tasks, "3": mark_done, "4": remove_task}

    while True:
        show_menu()
        choice = input("Enter a choice: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
