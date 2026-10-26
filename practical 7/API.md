# Task API

Generated from `app.py` by `generate_docs.py`.

This educational in-memory API demonstrates endpoint documentation. It does not start an HTTP server or persist data.

## Endpoints


### `GET /health`

Check whether the task API is available.

**Parameters:** None.

**Response example:**

```json
{
  "status": "ok"
}
```

### `GET /tasks`

Return all tasks.

**Parameters:** None.

**Response example:**

```json
[
  {
    "id": "1",
    "title": "Write API documentation"
  },
  {
    "id": "2",
    "title": "Validate generated docs"
  }
]
```

### `GET /tasks/{task_id}`

Return one task by its identifier.

**Parameters:** Path: `task_id` (string), the task identifier.

**Response example:**

```json
{
  "id": "1",
  "title": "Write API documentation"
}
```

### `POST /tasks`

Create a task with a non-empty title.

**Parameters:** JSON body: `title` (string, required, non-empty).

**Request example:**

```json
{
  "title": "Review generated documentation"
}
```

**Response example:**

```json
{
  "id": "3",
  "title": "Review generated documentation"
}
```
