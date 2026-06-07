# task_manager/validation.py
"""
Validation functions for task input data.

Each function returns a tuple:
    (True,  "")            – input is valid
    (False, "error msg")   – input is invalid, with a reason
"""

from datetime import datetime


def validate_task_title(title):
    """
    Validate a task title.

    Rules
    -----
    - Must be a string
    - Cannot be empty or only whitespace
    - Must be between 3 and 100 characters (after stripping)

    Parameters
    ----------
    title : str
        The title to validate.

    Returns
    -------
    tuple[bool, str]
        (True, "") on success; (False, error_message) on failure.

    Examples
    --------
    >>> validate_task_title("Groceries")
    (True, '')
    >>> validate_task_title("")
    (False, 'Title cannot be empty.')
    """
    if not isinstance(title, str):
        return False, "Title must be a string."
    if not title.strip():
        return False, "Title cannot be empty."
    if len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."
    if len(title.strip()) > 100:
        return False, "Title cannot exceed 100 characters."
    return True, ""


def validate_task_description(description):
    """
    Validate a task description.

    Rules
    -----
    - Must be a string
    - Cannot be empty or only whitespace
    - Must be between 5 and 500 characters (after stripping)

    Parameters
    ----------
    description : str
        The description to validate.

    Returns
    -------
    tuple[bool, str]
        (True, "") on success; (False, error_message) on failure.

    Examples
    --------
    >>> validate_task_description("Buy milk and eggs from the store")
    (True, '')
    >>> validate_task_description("ok")
    (False, 'Description must be at least 5 characters long.')
    """
    if not isinstance(description, str):
        return False, "Description must be a string."
    if not description.strip():
        return False, "Description cannot be empty."
    if len(description.strip()) < 5:
        return False, "Description must be at least 5 characters long."
    if len(description.strip()) > 500:
        return False, "Description cannot exceed 500 characters."
    return True, ""


def validate_due_date(due_date):
    """
    Validate a due-date string.

    Rules
    -----
    - Must be a non-empty string
    - Must match the format YYYY-MM-DD
    - Must not be a date already in the past

    Parameters
    ----------
    due_date : str
        The date string to validate, expected format YYYY-MM-DD.

    Returns
    -------
    tuple[bool, str]
        (True, "") on success; (False, error_message) on failure.

    Examples
    --------
    >>> validate_due_date("2099-01-01")
    (True, '')
    >>> validate_due_date("01-01-2024")
    (False, 'Due date must be in YYYY-MM-DD format (e.g. 2025-12-31).')
    """
    if not isinstance(due_date, str) or not due_date.strip():
        return False, "Due date cannot be empty."

    try:
        parsed = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format (e.g. 2025-12-31)."

    today = datetime.today().date()
    if parsed < today:
        return False, f"Due date cannot be in the past. Today is {today}."

    return True, ""