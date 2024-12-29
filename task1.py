tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added: {task}")
def update_task():
    if not tasks:
        print("No tasks available to update.")
        return
    show_tasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the new task description: ")
            print(f"Task updated: '{tasks[index]['task']}' -> '{new_task}'")
            tasks[index]["task"] = new_task
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_as_done():
    if not tasks:
        print("No tasks available to mark as done.")
        return
    show_tasks()
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task marked as done: {tasks[index]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Undone"
        print(f"{i}. {task['task']} [{status}]")

def main_menu():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Done")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            mark_as_done()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main_menu()
