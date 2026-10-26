"""Tests for the task API and its generated documentation."""

import unittest

from app import API_ENDPOINTS, create_task, get_task, health_check, list_tasks
from generate_docs import OUTPUT_PATH, generate_documentation


class TaskApiTests(unittest.TestCase):
    def test_health_check_returns_ok(self) -> None:
        self.assertEqual(health_check(), {"status": "ok"})

    def test_list_tasks_returns_task_copies(self) -> None:
        tasks = list_tasks()
        self.assertGreaterEqual(len(tasks), 2)
        self.assertIn("id", tasks[0])
        tasks[0]["title"] = "Changed in test"
        self.assertNotEqual(list_tasks()[0]["title"], "Changed in test")

    def test_get_task_returns_matching_task(self) -> None:
        self.assertEqual(
            get_task("1"),
            {"id": "1", "title": "Write API documentation"},
        )

    def test_get_task_reports_unknown_id(self) -> None:
        with self.assertRaisesRegex(KeyError, "was not found"):
            get_task("missing")

    def test_create_task_strips_title_and_stores_task(self) -> None:
        task = create_task("  Check the generated docs  ")
        self.assertEqual(task["title"], "Check the generated docs")
        self.assertEqual(get_task(task["id"]), task)

    def test_create_task_rejects_blank_title(self) -> None:
        with self.assertRaisesRegex(ValueError, "title must not be empty"):
            create_task("   ")


class GeneratedDocumentationTests(unittest.TestCase):
    def test_generated_file_matches_current_backend_metadata(self) -> None:
        self.assertEqual(
            OUTPUT_PATH.read_text(encoding="utf-8"),
            generate_documentation(),
        )

    def test_documentation_contains_every_endpoint(self) -> None:
        documentation = generate_documentation()
        for endpoint in API_ENDPOINTS:
            with self.subTest(endpoint=endpoint.path):
                self.assertIn(
                    f"### `{endpoint.method} {endpoint.path}`",
                    documentation,
                )

    def test_documentation_includes_request_validation_details(self) -> None:
        documentation = generate_documentation()
        self.assertIn("title` (string, required, non-empty)", documentation)
        self.assertIn('"title": "Review generated documentation"', documentation)


if __name__ == "__main__":
    unittest.main()
