# validation.py

from datetime import datetime


def validate_task_title(title):
    if len(title) == 0:
        return False, "Title cannot be empty."
    if len(title) < 3:
        return False, "Title must be at least 3 characters long."
    if len(title) > 100:
        return False, "Title cannot exceed 100 characters."
    return True, ""


def validate_task_description(description):
    if len(description) == 0:
        return False, "Description cannot be empty."
    if len(description) < 5:
        return False, "Description must be at least 5 characters long."
    if len(description) > 500:
        return False, "Description cannot exceed 500 characters."
    return True, ""


def validate_due_date(due_date):
    if len(due_date) == 0:
        return False, "Due date cannot be empty."
    try:
        parsed = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format (e.g. 2025-12-31)."
    today = datetime.today().date()
    if parsed < today:
        return False, f"Due date cannot be in the past. Today is {today}."
    return True, ""