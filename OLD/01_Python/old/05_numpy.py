"""
NUMPY NOTES – PYTHON (AI / ML ORIENTED)
Author: Vishal Mehra
Purpose: Numerical computing using NumPy
Style: Exam-oriented + Practical
"""

# =========================================================
# 1. INTRODUCTION TO NUMPY
# =========================================================

"""
NumPy (Numerical Python) is a fundamental library used for:
- Numerical computations
- Scientific computing
- Machine Learning
- Handling large multi-dimensional arrays

Advantages of NumPy:
- Faster than Python lists
- Uses less memory
- Provides vectorized operations
"""

import numpy as np


# =========================================================
# 2. CREATING NUMPY ARRAYS
# =========================================================

# Creating array from list
arr1 = np.array([1, 2, 3, 4, 5])

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Array with zeros
zeros_arr = np.zeros((3, 3))

# Array with ones
ones_arr = np.ones((2, 4))

# Identity matrix
identity_arr = np.eye(3)

# Range-based array
range_arr = np.arange(0, 10, 2)

# Evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5)


# =========================================================
# 3. ARRAY ATTRIBUTES
# =========================================================

"""
Important attributes:
- ndim  → number of dimensions
- shape → rows and columns
- size  → total elements
- dtype → data type
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.ndim      # Dimensions
arr.shape     # Shape
arr.size      # Total elements
arr.dtype     # Data type


# =========================================================
# 4. ARRAY INDEXING & SLICING
# =========================================================

arr = np.array([10, 20, 30, 40, 50])

# Indexing
first_element = arr[0]
last_element = arr[-1]

# Slicing
sub_array = arr[1:4]

# 2D indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

element = matrix[1, 2]     # Row 1, Column 2


# =========================================================
# 5. ARRAY OPERATIONS
# =========================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
add = a + b
sub = a - b
mul = a * b
div = a / b

# Scalar operations
scalar_mul = a * 5


# =========================================================
# 6. MATHEMATICAL FUNCTIONS
# =========================================================

arr = np.array([1, 4, 9, 16])

sqrt_arr = np.sqrt(arr)
log_arr = np.log(arr)
exp_arr = np.exp(arr)

sum_val = np.sum(arr)
mean_val = np.mean(arr)
max_val = np.max(arr)
min_val = np.min(arr)
std_val = np.std(arr)


# =========================================================
# 7. RESHAPING & FLATTENING
# =========================================================

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Reshape
reshaped = arr.reshape(3, 2)

# Flatten array
flat = arr.flatten()


# =========================================================
# 8. BROADCASTING
# =========================================================

"""
Broadcasting allows NumPy to perform operations on arrays
of different shapes without explicit loops.
"""

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

result = matrix + 10    # 10 added to every element


# =========================================================
# 9. BOOLEAN INDEXING
# =========================================================

arr = np.array([10, 20, 30, 40, 50])

# Condition-based selection
filtered = arr[arr > 25]


# =========================================================
# 10. RANDOM NUMBERS
# =========================================================

# Random numbers between 0 and 1
rand_arr = np.random.rand(5)

# Random integers
rand_int = np.random.randint(1, 100, size=5)

# Normal distribution
normal_arr = np.random.randn(5)


# =========================================================
# 11. NUMPY VS PYTHON LIST (EXAM POINT)
# =========================================================

"""
NumPy arrays:
- Faster execution
- Less memory
- Vectorized operations

Python Lists:
- Slower
- More memory
- No built-in mathematical operations
"""


# =========================================================
# 12. NUMPY IN MACHINE LEARNING
# =========================================================

"""
Uses of NumPy in ML:
- Feature matrices
- Vector operations
- Gradient calculations
- Preprocessing numerical data
"""

X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

y = np.array([1, 0, 1])


# =========================================================
# END OF NUMPY NOTES
# =========================================================
