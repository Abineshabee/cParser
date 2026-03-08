
---

# cParser – C Code Analyzer Using Python

cParser is a lightweight C language analysis tool written in Python that parses C source code, analyzes its syntax, and extracts information about function calls using an Abstract Syntax Tree (AST).

The project uses the Python library **pycparser**, which provides a complete parser for the C programming language written entirely in Python.

The goal of this project is to demonstrate how compilers and interpreters analyze source code by transforming it into an AST and traversing it to extract meaningful information such as function calls, arguments, and syntax validation.

This tool is designed primarily for educational purposes to help students and developers understand how source code parsing works internally.

---

# Project Repository

GitHub Repository:

[https://github.com/Abineshabee/cParser](https://github.com/Abineshabee/cParser)

---

# Project Objectives

The primary objectives of the cParser project include:

• Parsing C source code using Python
• Extracting function calls from C programs
• Demonstrating AST traversal
• Performing syntax validation on C code
• Teaching compiler and parser concepts

This project helps developers explore how compilers inspect and analyze source code before execution.

---

# Features

The cParser tool includes several capabilities:

• Parse C source code files
• Detect and print function calls
• Display arguments passed to functions
• Generate an Abstract Syntax Tree
• Validate syntax correctness
• Analyze C code snippets

---

# Technology Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Core implementation           |
| pycparser  | Parsing C language            |
| AST        | Code structure representation |

---

# Installation

Install the required library before running the program.

```bash
pip install pycparser
```

Clone the repository:

```bash
git clone https://github.com/Abineshabee/cParser.git
cd cParser
```

---

# How the Parser Works

The cParser program follows a simple parsing workflow:

1. The C source code is read.
2. The parser converts the code into tokens.
3. Tokens are used to build an Abstract Syntax Tree (AST).
4. The AST is traversed to identify function calls and arguments.
5. Syntax validation is performed during parsing.

---

# Abstract Syntax Tree (AST)

An AST represents the hierarchical structure of a program.

Example C code:

```c
int main() {
    printf("Hello World");
    return 0;
}
```

Simplified AST representation:

```
FileAST
 └── FuncDef
      └── main
           ├── FuncCall
           │    └── printf
           └── Return
```

The AST makes it possible to analyze and transform code programmatically.

---

# Program Structure

The project contains the following main components.

| Component           | Description                                 |
| ------------------- | ------------------------------------------- |
| FuncCallVisitor     | Visits AST nodes and detects function calls |
| show_func_calls     | Extracts function calls from a C file       |
| parse_and_print_ast | Parses code and displays AST                |
| check_syntax        | Validates syntax correctness                |

---

# Code Explanation

## Import Libraries

```python
from pycparser import c_parser, c_ast, parse_file
import sys
```

The parser imports:

* `c_parser` – main C parser
* `c_ast` – AST node classes
* `parse_file` – parses C source files

---

# FuncCallVisitor Class

This class traverses the AST and identifies function calls.

```python
class FuncCallVisitor(c_ast.NodeVisitor):
```

The visitor pattern is used to explore nodes in the AST.

---

## visit_FuncCall Method

```python
def visit_FuncCall(self, node):
    print(f'Function called: {node.name.name}')
```

This method is triggered whenever the parser encounters a function call node.

Example output:

```
Function called: printf
```

---

## Extracting Arguments

The visitor also prints arguments passed to the function.

Example code:

```python
printf("Hello", x);
```

Output:

```
Function called: printf
Arguments:
  string: Hello
  Variable: x
```

---

# show_func_calls Function

This function parses a C source file and extracts function calls.

```python
def show_func_calls(filename):
```

Example usage:

```bash
python parser.py sample.c
```

Example output:

```
Function called: printf
Arguments:
  string: x is less than y
```

---

# parse_and_print_ast Function

This function parses a C code snippet and prints the entire AST.

```python
def parse_and_print_ast(code):
```

Example:

```python
code = """
int main(){
  printf("Hello");
}
"""
```

Output (simplified):

```
FileAST
  FuncDef
    Decl
      FuncDecl
    Compound
      FuncCall
        ID: printf
```

---

# check_syntax Function

This function verifies whether the given C code contains syntax errors.

```python
def check_syntax(code):
```

Example:

```python
correct_code = "int main(){return 0;}"
print(check_syntax(correct_code))
```

Output:

```
True
```

Incorrect example:

```python
incorrect_code = "int main( { return 0; }"
```

Output:

```
False
```

---

# Example Execution

If the script is executed without arguments, it parses an example program.

Example C code used:

```c
int main() {
    int x = 5;
    int y = 10;

    if (x < y) {
        printf("x is less than y");
    }

    for (int i = 0; i < 10; i++) {
        printf("i: %d", i);
    }

    return 0;
}
```

Output example:

```
Function called: printf
Arguments:
  string: x is less than y

Function called: printf
Arguments:
  string: i: %d
  Variable: i
```

---

# Syntax Validation Example

The tool can check if code is syntactically valid.

Example output:

```
Checking syntax of various code snippets:

Correct code syntax: Correct
Incorrect code syntax: Incorrect
```

---

# Running the Tool

Run with a C file:

```bash
python parser.py example.c
```

Run without arguments:

```bash
python parser.py
```

This runs the built-in example program.

---

# Educational Value

This project demonstrates important compiler concepts:

* Abstract Syntax Tree (AST)
* Visitor design pattern
* Source code parsing
* Syntax validation
* Static code analysis

It is particularly useful for students learning:

* Compilers
* Programming language design
* Static analysis tools
* Code parsing techniques

---

# Future Improvements

Possible enhancements for the project include:

• Variable usage analysis
• Control flow graph generation
• Code complexity analysis
• Detection of unused variables
• Static security analysis
• Function dependency graphs

---

# Author

Abinesh N

GitHub
[https://github.com/Abineshabee](https://github.com/Abineshabee)

---



These will make your project look closer to a **mini compiler / code analysis tool**, which is **very impressive for recruiters and Linux Foundation reviewers**.
