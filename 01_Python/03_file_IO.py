# =========================================================
# Topics:
# 1. File I/O
# 2. Exception Handling
# 3. List Comprehensions
# 4. JSON Module
# =========================================================


# =========================================================
# 1. FILE I/O (INPUT / OUTPUT)
# =========================================================

# File I/O means reading data from files and writing data to files
# Python provides built-in functions to handle files


# -------------------------------
# Opening a File
# -------------------------------

# Syntax:
# file_object = open("filename", "mode")

# Example:
f = open("data.txt", "r")   # Opens file in read mode
f.close()                  # Always close the file after use


# -------------------------------
# File Modes
# -------------------------------

# r  -> Read mode (default), error if file does not exist
# w  -> Write mode, creates new file or overwrites existing file
# a  -> Append mode, adds content at the end
# r+ -> Read + Write (file must exist)
# w+ -> Write + Read (overwrites file)
# a+ -> Append + Read
# b  -> Binary mode (used for images, videos, etc.)


# -------------------------------
# Reading from a File
# -------------------------------

# 1. read() → Reads entire file as a single string
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()

# 2. readline() → Reads one line at a time
f = open("data.txt", "r")
line1 = f.readline()
line2 = f.readline()
f.close()

# 3. readlines() → Reads all lines into a list
f = open("data.txt", "r")
lines = f.readlines()
f.close()


# -------------------------------
# Writing to a File
# -------------------------------

# write() → Writes a single string
f = open("data.txt", "w")
f.write("Hello students!")
f.close()

# writelines() → Writes multiple lines
f = open("data.txt", "a")
f.writelines(["Line 1\n", "Line 2\n"])
f.close()


# -------------------------------
# Recommended Way: with open()
# -------------------------------

# with open() automatically closes the file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)


# -------------------------------
# Deleting a File
# -------------------------------

import os
os.remove("data.txt")   # Deletes the file


# =========================================================
# 2. EXCEPTION HANDLING
# =========================================================

# An exception is a runtime error
# If not handled, the program crashes
# Exception handling allows the program to continue execution


# -------------------------------
# Common Exceptions
# -------------------------------

# ZeroDivisionError      -> Division by zero
# NameError              -> Undefined variable
# FileNotFoundError      -> Missing file
# TypeError              -> Wrong data type


# -------------------------------
# Basic try-except Syntax
# -------------------------------

try:
    x = 10 / 0           # Error-prone code
except:
    print("Error occurred!")


# -------------------------------
# Handling Specific Exceptions
# -------------------------------

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# -------------------------------
# else Block
# -------------------------------

# else executes ONLY if no exception occurs

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)


# -------------------------------
# finally Block
# -------------------------------

# finally ALWAYS executes
# Used for cleanup tasks like closing files

try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")


# =========================================================
# 3. LIST COMPREHENSIONS
# =========================================================

# List comprehension is a short and elegant way to create lists
# It replaces long for-loops with one-line expressions


# -------------------------------
# Basic Syntax
# -------------------------------

# [expression for item in iterable]

nums = [x for x in range(1, 6)]
print(nums)   # Output: [1, 2, 3, 4, 5]


# -------------------------------
# With Condition
# -------------------------------

# [expression for item in iterable if condition]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)


# -------------------------------
# With if-else
# -------------------------------

# [true_expression if condition else false_expression for item in iterable]

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(labels)


# =========================================================
# 4. JSON MODULE
# =========================================================

# JSON (JavaScript Object Notation) is a lightweight data format
# Used to exchange data between programs, APIs, and web apps
# JSON format is very similar to Python dictionaries


import json


# -------------------------------
# Converting Python → JSON (dumps)
# -------------------------------

data = {
    "name": "John",
    "age": 25,
    "marks": [85, 90, 92]
}

json_string = json.dumps(data)
print(json_string)


# -------------------------------
# Converting JSON → Python (loads)
# -------------------------------

json_data = '{"name": "John", "age": 25}'
python_obj = json.loads(json_data)
print(python_obj["name"])


# -------------------------------
# Reading JSON from a File (json.load)
# -------------------------------

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)


# -------------------------------
# Writing JSON to a File (json.dump)
# -------------------------------

data = {
    "name": "Aisha",
    "city": "Delhi"
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)   # indent=4 makes JSON readable


# =========================================================
# END OF PYTHON FUNDAMENTALS – PART 5
# =========================================================
