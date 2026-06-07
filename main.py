# main.py
"""
Entry point for the Task Management System.

Directory layout expected:
    project/
    ├── main.py            ← you are here
    └── task_manager/
        ├── __init__.py
        ├── validation.py
        └── task_utils.py

Run:
    python main.py
"""

from task_manager import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

# ── Shared in-memory task store ───────────────────────────────────────────────
tasks = []


# ── Helper display functions ──────────────────────────────────────────────────

def print_separator(char="─", width=52):
    print(char * width)


def print_header():
    print_separator("═")
    print("        📋  TASK MANAGEMENT SYSTEM")
    print_separator("═")


def print_menu():
    print("\n  Choose an option:")
    print("  1.  Add a new task")
    print("  2.  Mark a task as complete")
    print("  3.  View pending tasks")
    print("  4.  Track overall progress")
    print("  5.  View ALL tasks")
    print("  6.  Exit")
    print_separator()


def display_task(task, number=None):
    """Print one task dict in a readable format."""
    prefix = f"  [{number}]" if number is not None else "  •"
    status = "✅  Complete" if task["completed"] else "⏳  Pending"
    print(f"{prefix} {task['title']}")
    print(f"       Description : {task['description']}")
    print(f"       Due date    : {task['due_date']}")
    print(f"       Status      : {status}")
    print()


def progress_bar(percentage, width=24):
    """Return a simple ASCII progress bar string."""
    filled = int(percentage / 100 * width)
    bar    = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {percentage:.1f}%"


# ── Menu action handlers ──────────────────────────────────────────────────────

def handle_add_task():
    """Prompt the user for task details and add the task."""
    print("\n  ── Add a New Task ──")
    title       = input("  Title       : ").strip()
    description = input("  Description : ").strip()
    due_date    = input("  Due date (YYYY-MM-DD) : ").strip()

    success, message = add_task(tasks, title, description, due_date)
    print(f"\n  {'✅' if success else '❌'}  {message}")


def handle_mark_complete():
    """Ask for a title and mark that task complete."""
    print("\n  ── Mark a Task as Complete ──")

    if not tasks:
        print("  ℹ️   No tasks yet. Please add a task first.")
        return

    title = input("  Enter the exact title of the task: ").strip()
    success, message = mark_task_as_complete(tasks, title)
    print(f"\n  {'✅' if success else '❌'}  {message}")


def handle_view_pending():
    """Display all pending (incomplete) tasks."""
    print("\n  ── Pending Tasks ──")
    pending = view_pending_tasks(tasks)

    if not pending:
        print("  🎉  No pending tasks – you're all caught up!")
        return

    print(f"  You have {len(pending)} pending task(s):\n")
    for i, task in enumerate(pending, start=1):
        display_task(task, number=i)


def handle_track_progress():
    """Show a progress summary and visual bar."""
    print("\n  ── Progress Report ──")
    pct, summary = calculate_progress(tasks)
    print(f"  📊  {summary}")
    if tasks:
        print(f"      {progress_bar(pct)}")


def handle_view_all():
    """Display every task regardless of status."""
    print("\n  ── All Tasks ──")

    if not tasks:
        print("  ℹ️   No tasks yet. Start by adding one!")
        return

    print(f"  Total tasks: {len(tasks)}\n")
    for i, task in enumerate(tasks, start=1):
        display_task(task, number=i)


# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    print_header()
    print("  Welcome! Manage your tasks below.\n")

    # ── Pre-load sample tasks so the app works out of the box ──
    samples = [
        ("Groceries",        "Shop at Market Basket for food",              "2026-12-26"),
        ("Python lab",       "Complete the Moringa task manager exercise",  "2026-08-01"),
        ("Read docs",        "Read the Python packaging documentation",     "2026-07-15"),
    ]
    for t, d, dd in samples:
        add_task(tasks, t, d, dd)
    # Pre-complete one to make the progress bar more interesting
    mark_task_as_complete(tasks, "Groceries")
    print(f"  (Loaded {len(samples)} sample tasks to get you started.)\n")

    # ── Interactive menu loop ──
    while True:
        print_menu()
        choice = input("  Your choice: ").strip()

        if   choice == "1": handle_add_task()
        elif choice == "2": handle_mark_complete()
        elif choice == "3": handle_view_pending()
        elif choice == "4": handle_track_progress()
        elif choice == "5": handle_view_all()
        elif choice == "6":
            print("\n  👋  Goodbye – stay productive!\n")
            break
        else:
            print("  ⚠️   Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()