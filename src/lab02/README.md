# Hello World

## Objectives

The objective of this assignment is to write a simple Python program that outputs "Hello, World!" or "Hello, [name]" depending on whether or not a name is provided as an argument to the script. 

## Requirements

- Write a Python script that contains a function named `main` which will be the entry point of the program.
- The `main` function should take the arguments passed to the script and use them to determine the output.
- If no arguments are passed, the script should output "Hello, World!".
- If one argument is passed, the script should output "Hello, [name]!", where [name] is the argument passed to the script.

## Example Usage

```
$ python hello.py
Hello, World!

$ python hello.py Young
Hello, Young!
```

## Self-Testing with make
It's recommended that you self-test your solution before submitting it. You can do this by running the following command in the terminal:

```
$ make
```

## Evaluation

Your solution will be evaluated based on:
- Correctness of the output when no argument is passed.
- Correctness of the output when an argument is passed.
- Correctness of the function definition and structure.

## Submission

Submit your solution as a single Python file named `main.py`.
