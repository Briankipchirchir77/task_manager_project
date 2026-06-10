try:
    from task_manager.validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date,
    )
except ImportError:
    from validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date,
    )


tasks = []


def add_task(title, description, due_date):
    try:
        title = validate_task_title(title)
        description = validate_task_description(description)
        due_date = validate_due_date(due_date)
    except ValueError as e:
        print(f"Error: {e}")
        return None

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")
    return task


def mark_task_as_complete(title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                print("Task is already complete.")
            else:
                task["completed"] = True
                print("Task marked as complete!")
            return True

    print(f"Task '{title}' not found.")
    return False


def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks.")
        return []

    print("Pending Tasks:")
    print("-" * 50)
    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")
        print(f"   {task['description']}")
    return pending


def calculate_progress(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks

    if not tasks_list:
        print("No tasks found.")
        return 0

    completed = len([task for task in tasks_list if task["completed"]])
    total = len(tasks_list)
    percentage = (completed / total) * 100
    print(f"Progress: {completed}/{total} tasks completed ({percentage:.1f}%)")
    return percentage
