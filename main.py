try:
    from task_manager.task_utils import (
        add_task,
        mark_task_as_complete,
        view_pending_tasks,
        calculate_progress,
    )
except ImportError:
    from task_utils import (
        add_task,
        mark_task_as_complete,
        view_pending_tasks,
        calculate_progress,
    )


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("       📝 TASK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add a Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")
    print("=" * 50)


def handle_add_task():
    """Handle user input for adding a task."""
    print("\n--- Add New Task ---")
    title = input("Enter task title       : ")
    description = input("Enter task description : ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    add_task(title, description, due_date)


def handle_mark_complete():
    """Handle user input for marking a task complete."""
    print("\n--- Mark Task as Complete ---")
    title = input("Enter the title or number of the task to complete: ")
    mark_task_as_complete(title)


def main():
    """Main entry point — runs the task management menu loop."""
    print("\nWelcome to the Task Management System! 🚀")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            handle_add_task()

        elif choice == "2":
            handle_mark_complete()

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("\n👋 Goodbye! Stay productive.\n")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()