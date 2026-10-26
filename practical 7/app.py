"""Small in-memory task API used to demonstrate API documentation generation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    """Describe an API endpoint for the documentation generator."""

    method: str
    path: str
    summary: str
    parameters: str
    request_example: str
    response_example: str


TASKS: dict[str, dict[str, str]] = {
    "1": {"id": "1", "title": "Write API documentation"},
    "2": {"id": "2", "title": "Validate generated docs"},
}
_next_task_id = 3


API_ENDPOINTS = (
    Endpoint(
        method="GET",
        path="/health",
        summary="Check whether the task API is available.",
        parameters="None.",
        request_example="",
        response_example='{"status": "ok"}',
    ),
    Endpoint(
        method="GET",
        path="/tasks",
        summary="Return all tasks.",
        parameters="None.",
        request_example="",
        response_example=(
            '[{"id": "1", "title": "Write API documentation"}, '
            '{"id": "2", "title": "Validate generated docs"}]'
        ),
    ),
    Endpoint(
        method="GET",
        path="/tasks/{task_id}",
        summary="Return one task by its identifier.",
        parameters="Path: `task_id` (string), the task identifier.",
        request_example="",
        response_example='{"id": "1", "title": "Write API documentation"}',
    ),
    Endpoint(
        method="POST",
        path="/tasks",
        summary="Create a task with a non-empty title.",
        parameters="JSON body: `title` (string, required, non-empty).",
        request_example='{"title": "Review generated documentation"}',
        response_example=(
            '{"id": "3", "title": "Review generated documentation"}'
        ),
    ),
)


def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}


def list_tasks() -> list[dict[str, str]]:
    """Return a copy of every task."""
    return [task.copy() for task in TASKS.values()]


def get_task(task_id: str) -> dict[str, str]:
    """Return a task, or raise KeyError when its identifier is unknown."""
    try:
        return TASKS[task_id].copy()
    except KeyError as error:
        raise KeyError(f"Task {task_id!r} was not found") from error


def create_task(title: str) -> dict[str, str]:
    """Create and return a task; reject titles containing only whitespace."""
    global _next_task_id

    normalized_title = title.strip()
    if not normalized_title:
        raise ValueError("title must not be empty")

    task_id = str(_next_task_id)
    _next_task_id += 1
    task = {"id": task_id, "title": normalized_title}
    TASKS[task_id] = task
    return task.copy()
