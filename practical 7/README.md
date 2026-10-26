# Practical 7: AI-Generated API Documentation

## Aim

Generate API documentation from backend code with an AI coding assistant and
validate the generated documentation against the source API.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI assistant
- Python standard library (`json`, `unittest`)

## Step 1 – Backend code: `app.py` (excerpt)

`app.py` provides a small in-memory task API with health, list, get, and create
operations. Its `API_ENDPOINTS` metadata describes the public methods, paths,
parameters, and JSON examples. The sample focuses on documentation and does not
start an HTTP server or persist task data.

For a screenshot of the backend source from the repository root:

```powershell
Get-Content ".\practical 7\app.py"
```

## Step 2 – Documentation generator: `generate_docs.py`

The generator reads `API_ENDPOINTS` from `app.py` and renders each endpoint into
Markdown, including request and response examples.

For a screenshot of the generator source:

```powershell
Get-Content ".\practical 7\generate_docs.py"
```

## Step 3 – Generate the documentation

Run from the repository root in the VS Code PowerShell terminal:

```powershell
python ".\practical 7\generate_docs.py"
```

Expected output:

```text
Generated API.md (4 endpoints)
```

Take a screenshot showing the command and output.

## Step 4 – Generated documentation: `API.md` (excerpt)

The generated reference is saved as `API.md`. To display it in the terminal:

```powershell
Get-Content ".\practical 7\API.md"
```

Take a screenshot showing the generated endpoint documentation.

## Step 5 – Validation tests: `test_docs.py` (excerpt)

The tests validate backend behavior, check that every declared endpoint appears
in the generated documentation, and ensure the checked-in `API.md` matches the
current generator output.

Run the tests from the repository root:

```powershell
python -m unittest discover -s ".\practical 7" -p "test_*.py" -v
```

The expected result is 9 passing tests and `OK`. Take a screenshot showing the
command and test report.

## Conclusion

The generator produces a consistent Markdown API reference from backend
metadata. Automated tests verify the endpoint coverage, examples, and generated
file, making documentation drift detectable.
