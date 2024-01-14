import os

def display_menu():
    print("===== To-Do List Application =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Quit")

def view_todo_list():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks in the to-do list.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No to-do list found. Creating a new one.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully.")

def complete_task():
    view_todo_list()
    try:
        task_number = int(input("Enter the number of the task to mark as complete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{completed_task.strip()}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
