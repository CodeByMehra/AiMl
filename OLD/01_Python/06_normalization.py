# ============================================================
# TOPIC: DATA NORMALIZATION (Z-SCORE NORMALIZATION)
# LANGUAGE: Python (NumPy)
# PURPOSE: Exam notes + practical understanding
# ============================================================

# ------------------------------------------------------------
# DEFINITION:
# Normalization is a data preprocessing technique used to
# scale numerical values so that they have:
# - Mean = 0
# - Standard Deviation = 1
#
# This helps machine learning algorithms converge faster
# and prevents features with large values from dominating.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Z-SCORE NORMALIZATION FORMULA:
#
#           Z = (X - μ) / σ
#
# Where:
# X  = Original value
# μ  = Mean of the dataset
# σ  = Standard Deviation of the dataset
# Z  = Normalized value
# ------------------------------------------------------------


# ------------------------------------------------------------
# IMPORTING NUMPY LIBRARY
# NumPy is used for numerical operations in Python
# ------------------------------------------------------------
import numpy as np


# ------------------------------------------------------------
# CREATING A NUMPY ARRAY
# This is a 2D array with 2 rows and 2 columns
# ------------------------------------------------------------
arr = np.array([[1, 2],
                [3, 4]])


# ------------------------------------------------------------
# CALCULATING MEAN (μ)
# Mean = Sum of all elements / Total number of elements
# np.mean() computes the average of all values in the array
# ------------------------------------------------------------
mean = np.mean(arr)


# ------------------------------------------------------------
# CALCULATING STANDARD DEVIATION (σ)
# Standard deviation measures how much values deviate
# from the mean.
# np.std() computes standard deviation of the array
# ------------------------------------------------------------
std_dev = np.std(arr)


# ------------------------------------------------------------
# APPLYING Z-SCORE NORMALIZATION
# Each element is transformed using the formula:
# (value - mean) / standard deviation
# ------------------------------------------------------------
normalized_arr = (arr - mean) / std_dev


# ------------------------------------------------------------
# DISPLAYING THE NORMALIZED ARRAY
# ------------------------------------------------------------
print(normalized_arr)


# ------------------------------------------------------------
# OUTPUT INTERPRETATION:
# - Negative values → below mean
# - Positive values → above mean
# - Mean of normalized data ≈ 0
# - Standard deviation ≈ 1
# ------------------------------------------------------------


# ------------------------------------------------------------
# IMPORTANT POINTS (EXAM ORIENTED):
#
# 1. Z-score normalization is also called standardization.
# 2. It is sensitive to outliers.
# 3. Used in algorithms like:
#    - Linear Regression
#    - Logistic Regression
#    - KNN
#    - SVM
#    - Neural Networks
# 4. Normalization improves numerical stability.
# ------------------------------------------------------------
