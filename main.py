# main.py

from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

tasks = []


def main():
    while True:
        print("\n========== Task Manager ==========")
        print("1. Add a new task")
        print("2. Mark a task as complete")
        print("3. View pending tasks")
        print("4. Track progress")
        print("5. Exit")
        print("==================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title       = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date    = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            mark_task_as_complete(tasks, title)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            calculate_progress(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()