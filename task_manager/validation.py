from datetime import datetime


def validate_task_title(title):
    """Validate task title is not empty and within length limits."""
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    if len(title.strip()) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    return title.strip()


def validate_task_description(description):
    """Validate task description is not empty and within length limits."""
    if not description or not description.strip():
        raise ValueError("Description cannot be empty.")
    if len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    if len(description.strip()) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return description.strip()


def validate_due_date(due_date):
    """Validate due date is in YYYY-MM-DD format and not in the past."""
    if not due_date or not due_date.strip():
        raise ValueError("Due date cannot be empty.")
    if len(due_date.strip()) != 10:
        raise ValueError("Due date must be exactly 10 characters in YYYY-MM-DD format.")
    try:
        date_obj = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format (e.g. 2026-12-31).")
    if date_obj.date() < datetime.today().date():
        raise ValueError("Due date cannot be in the past.")
    return due_date.strip()