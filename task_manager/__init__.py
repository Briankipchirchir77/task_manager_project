# task_manager/__init__.py
# Makes 'task_manager' a Python package.
# Expose the most-used functions at the package level so main.py
# can do:  from task_manager import add_task, ...

from .task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)