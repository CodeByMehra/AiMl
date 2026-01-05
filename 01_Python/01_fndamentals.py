"""
===========================================================
PYTHON FUNDAMENTALS – PART 1
Topics Covered:
1. Output (print)
2. Python Character Set
3. Variables
4. Variable Naming Rules
5. Data Types
6. Type Conversion & Casting
7. Operators
8. Operator Precedence
9. Input Function
10. Unary Operators
===========================================================

NOTE:
- Theory is written using comments (#)
- Executable examples are provided for practice
"""

# ===========================================================
# 1. OUTPUT IN PYTHON
# ===========================================================

# print() is used to display output on the screen
print("Hello World")

# Printing numbers
print(3.14)
print(2 + 3)

# Printing multiple values
print("Hello", "from", "Python")

# Each print statement outputs on a new line
print("Line 1")
print("Line 2")

# ===========================================================
# 2. PYTHON CHARACTER SET
# ===========================================================

# Python supports:
# - English letters (A-Z, a-z)
# - Digits (0-9)
# - Special symbols (+, -, *, /, %, etc.)
# - Whitespaces and escape characters (\n, \t)
# - ASCII and Unicode characters

print("A to Z, a to z, 0 to 9, symbols & unicode ✓")

# ===========================================================
# 3. VARIABLES IN PYTHON
# ===========================================================

# Variables are containers used to store data values

name = "Shradha"
age = 30
PI = 3.14
word = "artificial intelligence"

print("Name:", name)
print("Age:", age)
print("Value of PI:", PI)
print("Word:", word)

# Python is dynamically typed (no need to declare type)

# ===========================================================
# 4. VARIABLE NAMING RULES
# ===========================================================

# Valid variable names
student_name = "Bob"
_marks = 85
age2 = 21

# Invalid variable names (commented to avoid error)
# 2name = "Alice"     # Cannot start with number
# class = 10          # 'class' is a Python keyword

# Python is case-sensitive
Age = 25
age = 20
print("Age:", Age)
print("age:", age)

# ===========================================================
# 5. DATA TYPES IN PYTHON
# ===========================================================

# int
x = 10
print(type(x))

# float
pi = 3.14
print(type(pi))

# string
name = "Shradha"
print(type(name))

# boolean
isStudent = True
print(type(isStudent))

# NoneType
empty_var = None
print(type(empty_var))

# Automatic type conversion
a = 5
b = 3.0
print(a + b)  # result is float

# ===========================================================
# 6. TYPE CONVERSION & TYPE CASTING
# ===========================================================

# Explicit type casting
x = 10
y = float(x)
z = str(x)

print(y)
print(z)
print(type(y))
print(type(z))

# Common type conversion functions:
# int(), float(), str(), bool(), list(), tuple()

# ===========================================================
# 7. OPERATORS IN PYTHON
# ===========================================================

# -------------------------------
# 7.1 Arithmetic Operators
# -------------------------------

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a ** b)  # Power

# -------------------------------
# 7.2 Relational Operators
# -------------------------------

print(a == b)  # Equal to
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal
print(a <= b)  # Less than or equal

# -------------------------------
# 7.3 Assignment Operators
# -------------------------------

x = 10
print(x)

x += 5   # x = x + 5
print(x)

x -= 3   # x = x - 3
print(x)

x *= 2   # x = x * 2
print(x)

x /= 4   # x = x / 4
print(x)

x %= 3   # x = x % 3
print(x)

x **= 2  # x = x ** 2
print(x)

# -------------------------------
# 7.4 Logical Operators
# -------------------------------

x = 10
y = 20
z = 5

print(x > z and y > x)   # AND
print(x > y or y > z)    # OR
print(not (x > y))       # NOT

# ===========================================================
# 8. OPERATOR PRECEDENCE
# ===========================================================

# Order of execution:
# (), **, unary + -, *, /, %, + -, comparisons, not, and, or, assignment

result = (2 + 3) * 4 ** 2
print(result)

# ===========================================================
# 9. INPUT FUNCTION
# ===========================================================

# input() takes input from user as STRING

# Uncomment to test manually
# name = input("Enter your name: ")
# print(name)
# print(type(name))

# Type conversion with input
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum =", a + b)

# Average of two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# avg = (a + b) / 2
# print("Average =", avg)

# ===========================================================
# 10. UNARY OPERATORS
# ===========================================================

x = 5
y = -x   # Unary minus

print(x)
print(y)

# Unary plus (+x) is rarely used since numbers are positive by default

# ===========================================================
# END OF PYTHON FUNDAMENTALS – PART 1
# ===========================================================

print("Keep Learning & Keep Exploring Python!")
