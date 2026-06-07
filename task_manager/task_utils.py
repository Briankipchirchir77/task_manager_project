# task_manager/task_utils.py
"""
Core task-management functions.

All functions operate on a plain Python list of task dictionaries.
The task dictionary structure is:

    task = {
        "title":       str,   # short name for the task
        "description": str,   # details about what needs to be done
        "due_date":    str,   # deadline in YYYY-MM-DD format
        "completed":   bool,  # False = pending, True = done
    }
"""

from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)


def add_task(tasks, title, description, due_date):
    """
    Validate inputs and, if valid, append a new task to *tasks*.

    Parameters
    ----------
    tasks       : list   – the shared task list (mutated in-place)
    title       : str    – task title
    description : str    – task description
    due_date    : str    – deadline in YYYY-MM-DD format

    Returns
    -------
    tuple[bool, str]
        (True,  success_message) – task was added
        (False, error_message)   – validation failed; list unchanged

    Example
    -------
    >>> tasks = []
    >>> add_task(tasks, "Groceries", "Buy milk and eggs", "2099-12-01")
    (True, "Task 'Groceries' added successfully!")
    >>> len(tasks)
    1
    """
    # Validate every field before touching the list
    ok, err = validate_task_title(title)
    if not ok:
        return False, f"Invalid title – {err}"

    ok, err = validate_task_description(description)
    if not ok:
        return False, f"Invalid description – {err}"

    ok, err = validate_due_date(due_date)
    if not ok:
        return False, f"Invalid due date – {err}"

    task = {
        "title":       title.strip(),
        "description": description.strip(),
        "due_date":    due_date.strip(),
        "completed":   False,
    }
    tasks.append(task)
    return True, f"Task '{task['title']}' added successfully!"


def mark_task_as_complete(tasks, title):
    """
    Find a task by title and set its *completed* flag to True.

    The search is case-insensitive. Only the first matching task is updated.

    Parameters
    ----------
    tasks : list – the shared task list
    title : str  – title of the task to mark as complete

    Returns
    -------
    tuple[bool, str]
        (True,  success_message) – task found and updated
        (False, error_message)   – not found, or already complete

    Example
    -------
    >>> tasks = [{"title": "Groceries", "description": "...",
    ...           "due_date": "2099-12-01", "completed": False}]
    >>> mark_task_as_complete(tasks, "groceries")
    (True, "Task 'Groceries' marked as complete. Well done!")
    """
    if not title or not title.strip():
        return False, "Please provide the title of the task to complete."

    needle = title.strip().lower()

    for task in tasks:
        if task["title"].lower() == needle:
            if task["completed"]:
                return False, f"Task '{task['title']}' is already marked as complete."
            task["completed"] = True
            return True, f"Task '{task['title']}' marked as complete. Well done!"

    return False, f"No task found with the title '{title.strip()}'."


def view_pending_tasks(tasks):
    """
    Return all tasks that have not yet been completed.

    Parameters
    ----------
    tasks : list – the shared task list

    Returns
    -------
    list
        A (possibly empty) list of task dictionaries where completed == False.

    Example
    -------
    >>> tasks = [
    ...     {"title": "A", "description": "...", "due_date": "2099-01-01", "completed": True},
    ...     {"title": "B", "description": "...", "due_date": "2099-01-01", "completed": False},
    ... ]
    >>> view_pending_tasks(tasks)
    [{"title": "B", ...}]
    """
    return [task for task in tasks if not task["completed"]]


def calculate_progress(tasks):
    """
    Calculate the percentage of completed tasks.

    Parameters
    ----------
    tasks : list – the shared task list

    Returns
    -------
    tuple[float, str]
        (percentage, human-readable summary)
        percentage is 0.0 when the list is empty.

    Example
    -------
    >>> tasks = [
    ...     {"title": "A", ..., "completed": True},
    ...     {"title": "B", ..., "completed": False},
    ... ]
    >>> calculate_progress(tasks)
    (50.0, '1 of 2 tasks completed (50.00%)')
    """
    total = len(tasks)
    if total == 0:
        return 0.0, "No tasks yet – add some tasks to start tracking progress!"

    done = sum(1 for t in tasks if t["completed"])
    pct  = (done / total) * 100
    label = "task" if total == 1 else "tasks"
    summary = f"{done} of {total} {label} completed ({pct:.2f}%)"
    return pct, summary