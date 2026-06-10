from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# In-memory task list
tasks = []


def add_task(title, description, due_date):
    """Add a new task after validating inputs."""
    try:
        validated_title = validate_task_title(title)
        validated_description = validate_task_description(description)
        validated_due_date = validate_due_date(due_date)

        task = {
            "title": validated_title,
            "description": validated_description,
            "due_date": validated_due_date,
            "completed": False
        }
        tasks.append(task)
        print(f"\n✅ Task '{validated_title}' added successfully!")
        return task

    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return None


def mark_task_as_complete(title):
    """Mark a task as complete by title."""
    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                print(f"\n⚠️  Task '{title}' is already complete.")
            else:
                task["completed"] = True
                print(f"\n✅ Task '{title}' marked as complete!")
            return
    print(f"\n❌ Task '{title}' not found.")


def view_pending_tasks():
    """View all tasks that are not yet complete."""
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("\n🎉 No pending tasks! You're all caught up.")
        return []

    print("\n📋 Pending Tasks:")
    print("-" * 50)
    for i, task in enumerate(pending, 1):
        print(f"{i}. Title      : {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date   : {task['due_date']}")
        print("-" * 50)
    return pending


def calculate_progress():
    """Calculate and display the percentage of completed tasks."""
    if not tasks:
        print("\n⚠️  No tasks found. Add some tasks first.")
        return 0

    completed = len([task for task in tasks if task["completed"]])
    total = len(tasks)
    percentage = (completed / total) * 100

    print(f"\n📊 Progress: {completed}/{total} tasks completed ({percentage:.1f}%)")

    # Visual progress bar
    bar_length = 30
    filled = int(bar_length * completed / total)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"   [{bar}] {percentage:.1f}%")

    return percentage