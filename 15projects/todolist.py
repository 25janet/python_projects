to_do_list = []

def show_menu():
    while True:
        print("\n===== TASK MANAGER MENU =====")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark a task as done")
        print("5. Exit")

        try:
            choice = int(input("Choose the action you wish to perform (1/2/3/4/5): "))
            match choice:
                case 1:
                    add_task()
                case 2:
                    view_tasks()
                case 3:
                    delete_task()
                case 4:
                    mark_done()
                case 5:
                    exit_tasklist()
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def add_task():
    task = input("Enter the task to be added: ").strip()
    if task:
        to_do_list.append({"task": task, "done": False})
        print(f"'{task}' has been added to the list.")
    else:
        print("You did not enter a task.")

def view_tasks():
    if not to_do_list:
        print("Your task list is empty.")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(to_do_list, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} - {status}")

def delete_task():
    if not to_do_list:
        print("Your task list is empty.")
        return

    view_tasks()
    try:
        index = int(input("Enter the task number to be removed: "))
        if 1 <= index <= len(to_do_list):
            removed = to_do_list.pop(index - 1)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    if not to_do_list:
        print("Your task list is empty.")
        return

    view_tasks()
    try:
        index = int(input("Enter the task number to mark as done: "))
        if 1 <= index <= len(to_do_list):
            to_do_list[index - 1]["done"] = True
            print(f"Task {index} marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def exit_tasklist():
    print("You are exiting the task manager. Goodbye!")
    exit()

# Start of the program
print("Welcome to the Task Manager!")
choice = input("Enter '1' to show the menu or any other key to quit: ").strip()
if choice == "1":
    show_menu()
else:
    print("Quitting the program.")
    exit()
