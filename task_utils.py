# task_utils.py

from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    ok, err = validate_task_title(title)
    if not ok:
        print(f"Error: {err}")
        return

    ok, err = validate_task_description(description)
    if not ok:
        print(f"Error: {err}")
        return

    ok, err = validate_due_date(due_date)
    if not ok:
        print(f"Error: {err}")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                print(f"Task '{task['title']}' is already marked as complete.")
                return
            task["completed"] = True
            print(f"Task '{task['title']}' marked as complete.")
            return
    print(f"No task found with the title '{title}'.")


def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        print(f"You have {len(pending)} pending task(s):")
        for i, task in enumerate(pending, start=1):
            print(f"  {i}. {task['title']} - Due: {task['due_date']}")
            print(f"     {task['description']}")
    return pending


def calculate_progress(tasks):
    total = len(tasks)
    if total == 0:
        print("No working currently.")
        return
    done = 0
    for task in tasks:
        if task["completed"]:
            done += 1
    percentage = (done / total) * 100
    print(f"Progress: {done} of {total} tasks completed ({percentage:.2f}%)")