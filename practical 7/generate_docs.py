"""Generate API.md from the endpoint metadata in app.py."""

import json
from pathlib import Path

from app import API_ENDPOINTS, Endpoint

OUTPUT_PATH = Path(__file__).with_name("API.md")


def render_endpoint(endpoint: Endpoint) -> str:
    """Render one endpoint description as a Markdown section."""
    lines = [
        f"### `{endpoint.method} {endpoint.path}`",
        "",
        endpoint.summary,
        "",
        f"**Parameters:** {endpoint.parameters}",
    ]
    if endpoint.request_example:
        lines.extend(
            [
                "",
                "**Request example:**",
                "",
                "```json",
                json.dumps(json.loads(endpoint.request_example), indent=2),
                "```",
            ]
        )
    lines.extend(
        [
            "",
            "**Response example:**",
            "",
            "```json",
            json.dumps(json.loads(endpoint.response_example), indent=2),
            "```",
        ]
    )
    return "\n".join(lines)


def generate_documentation() -> str:
    """Build the complete API reference from the backend endpoint metadata."""
    sections = [
        "# Task API",
        "",
        "Generated from `app.py` by `generate_docs.py`.",
        "",
        (
            "This educational in-memory API demonstrates endpoint "
            "documentation. It does not start an HTTP server or persist data."
        ),
        "",
        "## Endpoints",
        "",
    ]
    header = "\n".join(sections)
    endpoint_sections = (
        render_endpoint(endpoint) for endpoint in API_ENDPOINTS
    )
    return header + "\n\n" + "\n\n".join(endpoint_sections) + "\n"


def main() -> None:
    """Write the generated reference and report its output path."""
    documentation = generate_documentation()
    OUTPUT_PATH.write_text(documentation, encoding="utf-8")
    print(f"Generated {OUTPUT_PATH.name} ({len(API_ENDPOINTS)} endpoints)")


if __name__ == "__main__":
    main()
