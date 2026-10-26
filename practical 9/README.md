# Practical 9: AI-Generated UML/ER/Architecture Diagrams

## Aim

Generate Graphviz diagram source from a textual description with an AI
assistant, render it, and verify both the diagram source and rendered output.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI tool
- Graphviz (`dot`) to render the diagram
- Python standard library (`argparse`, `re`, `unittest`, `xml.etree`)

Install Graphviz on Windows if the `dot` command is not available. For example,
with Chocolatey in an elevated PowerShell terminal:

```powershell
choco install graphviz -y
```

Restart the terminal after installation and confirm Graphviz is available:

```powershell
dot -V
```

## Step 1 – Textual description (`description.txt`)

The description specifies four library entities, their key attributes, and
one-to-many relationships between members, books, loans, and reservations.
Display it for the screenshot:

```powershell
Get-Content ".\practical 9\description.txt"
```

## Step 2 – Diagram source: `library_er.dot` (excerpt)

The DOT source defines the ER entities as record-shaped nodes and the
relationships as labeled directed edges. Show it in the terminal:

```powershell
Get-Content ".\practical 9\library_er.dot"
```

## Step 3 – Render the diagram with Graphviz

Run from the repository root:

```powershell
dot -Tsvg ".\practical 9\library_er.dot" -o ".\practical 9\library_er.svg"
```

The command should finish without errors. Take a screenshot with the command
and its terminal result.

## Step 4 – Rendered diagram

Open `practical 9\library_er.svg` in a browser or VS Code to capture the
rendered ER diagram. To confirm the output file exists in PowerShell:

```powershell
Get-Item ".\practical 9\library_er.svg" | Select-Object Name, Length
```

## Step 5 – Verification script: `verify_diagram.py` (excerpt)

The checker verifies that the DOT declares all four entities and all four
relationships, then parses the SVG and checks that its rendered entity labels
are present.

```powershell
Get-Content ".\practical 9\verify_diagram.py"
```

## Step 6 – Verification run

Run after rendering the SVG:

```powershell
python ".\practical 9\verify_diagram.py"
```

Expected output:

```text
Diagram verification:
[PASS] DOT source: all 4 entities and 4 relationships are declared
[PASS] Rendered SVG: valid SVG includes all 4 entity labels
Verification result: PASS
```

Run the verification tests from the repository root:

```powershell
python -m unittest discover -s ".\practical 9" -p "test_*.py" -v
```

The expected result is 4 passing tests and `OK`.

## Conclusion

The DOT source captures the entities and relationships from the textual
description. Graphviz renders it as SVG, and the verification script checks
both required source relationships and visible rendered entity labels.
