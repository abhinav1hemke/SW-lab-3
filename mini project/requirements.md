# Requirements: Simple Expense Tracker

## Purpose

Create a small command-line application that helps one person record and review
everyday expenses. It is an educational local application, not a banking or
accounting system.

## Functional requirements

- **FR-1:** A user can add an expense with a description, positive amount,
  category, and date.
- **FR-2:** If no date is supplied, the application uses today's date.
- **FR-3:** A user can list saved expenses with their details.
- **FR-4:** A user can view the total amount spent and totals grouped by
  category.
- **FR-5:** Expenses persist as JSON between application runs.
- **FR-6:** A user can choose a data-file path, which supports isolated tests
  and alternate local data files.
- **FR-7:** The application reports invalid amounts and dates as user-facing
  errors and does not save an invalid expense.

## Non-functional requirements

- Use Python's standard library; no database or third-party runtime package is
  required.
- Keep the code separated into data model, storage, and command-line interface
  modules.
- Store money with decimal arithmetic and display amounts to two decimal
  places.
- Provide automated tests that run with Python's built-in `unittest`.

## Out of scope

- User accounts, cloud synchronization, payment processing, budgets, and
  graphical user interfaces.
