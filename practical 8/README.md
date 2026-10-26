# Practical 8: AI-Based Conversion of Requirements into User Stories

## Aim

Convert an SRS excerpt into user stories and acceptance criteria with an AI
coding assistant, then evaluate completeness against the source requirements.

## Tools

- Python 3
- GitHub Copilot, Windsurf, or Ollama as the AI tool
- Python standard library (`argparse`, `re`, `unittest`)

## Step 1 – Input: SRS excerpt (`srs_excerpt.txt`)

The sample SRS describes a simple account portal with requirements for account
registration, sign-in/sign-out, and password reset.

From the repository root, display the source excerpt for a screenshot:

```powershell
Get-Content ".\practical 8\srs_excerpt.txt"
```

## Step 2 – Draft 1 of the user stories (excerpt)

Draft 1 contains two stories. It omits the password-reset requirement and has
incomplete acceptance criteria, so the checker can demonstrate gaps.

```powershell
Get-Content ".\practical 8\draft1.md"
```

## Step 3 – Completeness checker: `check_stories.py` (excerpt)

The checker compares requirement IDs in the SRS and stories, checks the
`As a / I want / so that` story format, and requires at least two
Given/When/Then acceptance criteria per story.

```powershell
Get-Content ".\practical 8\check_stories.py"
```

## Step 4 – Evaluate Draft 1

Run the checker against Draft 1:

```powershell
python ".\practical 8\check_stories.py" ".\practical 8\draft1.md"
```

Expected report: **1/3 checks passed (33%)**. Requirement coverage fails
because `REQ-03` is missing, and acceptance criteria fail because each story
has fewer than two valid Given/When/Then criteria.

## Step 5 – Revised user stories (excerpt)

The revised set covers all three requirements and provides at least two
Given/When/Then acceptance criteria for every story.

```powershell
Get-Content ".\practical 8\revised_stories.md"
```

## Step 6 – Re-check the revised stories

```powershell
python ".\practical 8\check_stories.py" ".\practical 8\revised_stories.md"
```

Expected report: **3/3 checks passed (100%)**, with an evaluation result of
`COMPLETE`.

Run the validation tests from the repository root:

```powershell
python -m unittest discover -s ".\practical 8" -p "test_*.py" -v
```

The expected result is 4 passing tests and `OK`. The tests confirm that the
first draft is reported incomplete and the revised stories pass all checks.

## Conclusion

The checker makes requirement coverage, story structure, and acceptance
criteria completeness measurable. Draft 1’s gaps are visible in the evaluation
report, while the revised stories pass the same checks.
