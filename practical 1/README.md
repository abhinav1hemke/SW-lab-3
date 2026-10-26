# Practical 1: Installation and Exploration of an AI Code Assistant

## Aim

Configure an AI code assistant in an IDE, request Java boilerplate, and compare
the assistant's output with a manually written implementation.

## Tools

- Java JDK (JDK 17 or newer recommended)
- Visual Studio Code or another Java IDE
- GitHub Copilot, Windsurf, or Ollama as the AI assistant

## Configure the assistant

In VS Code, install the **Extension Pack for Java** and the chosen assistant
extension. For GitHub Copilot, sign in when VS Code requests authorization. For
Windsurf, install and sign in to its editor. For Ollama, install Ollama, start a
local model, and configure the corresponding IDE extension to use it. Confirm
that the assistant can answer a simple code question before continuing.

## Comparison task

Ask the assistant:

> Create a simple Java `Student` class with an ID, name, and course. Include a
> constructor, a method to display the values, and a `main` method that prints
> one sample student. Keep the code beginner-friendly.

Review the generated response, check that it compiles, and save the accepted
AI-assisted version as
`practical 1\ai_generated\Student.java`. The checked-in file is a sample of
typical AI-generated boilerplate for comparison; adapt it to the exact code
your assistant generates and note any changes you make.

## AI Generated Output (`Student.java`)

The sample AI-style implementation includes a default constructor,
parameterized constructor, getters, setters, and a display method:

```powershell
Get-Content ".\practical 1\ai_generated\Student.java"
```

## Manually Written Code

Write the same small program yourself and save it as
`practical 1\manually_written\Student.java`. The manual example uses final
fields and includes only the constructor and display method needed by the
program:

```powershell
Get-Content ".\practical 1\manually_written\Student.java"
```

## Compile and run the comparison

Run these commands from the repository root. Compile each same-named class to
a separate output folder so the examples do not conflict:

```powershell
javac -d ".\practical 1\build\ai" ".\practical 1\ai_generated\Student.java"
java -cp ".\practical 1\build\ai" Student

javac -d ".\practical 1\build\manual" ".\practical 1\manually_written\Student.java"
java -cp ".\practical 1\build\manual" Student
```

Both programs should print:

```text
Student ID: 1
Name: Asha
Course: Computer Science
```

Take screenshots of the AI-generated output, manually written code, and
terminal runs.

## Comparison

Both versions produce the same visible output. The AI-style example supplies
extra reusable boilerplate (a default constructor and getters/setters). The
manually written version is shorter and makes the student fields immutable.
The generated code still needs review: decide whether the additional methods
are useful, check that the class compiles, and compare its behavior with the
task before using it.

## Conclusion

This practical demonstrates configuring an IDE assistant and reviewing its
Java output alongside a manual implementation. Compilation and matching
program output provide a simple check of correctness; shorter code is not
automatically better if the application needs the extra generated methods.
