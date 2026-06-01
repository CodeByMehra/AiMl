"""
DATA PROCESSING & ANALYSIS – PYTHON NOTES
Author: Vishal Mehra
Purpose: Clean, analyze, and extract insights from data
Style: Exam-oriented + Practical
"""

# =========================================================
# 1. LOADING DATA
# =========================================================

import json

def load_data(filename):
    """
    Loads JSON data from a file.

    Parameters:
    filename (str): Path to JSON file

    Returns:
    list: List of dictionaries (data)
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# =========================================================
# 2. DATA CLEANING FUNCTION
# =========================================================

def clean_data(data):
    """
    Cleans and structures raw user data.
    - Converts text ratings to numbers
    - Handles missing age values
    - Removes duplicate users
    """

    text_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    cleaned_data = []
    unique_users = set()

    for user in data:
        # ---------- Clean Rating ----------
        raw_rating = user["rating"].strip().lower()

        if raw_rating in text_to_num:
            raw_rating = text_to_num[raw_rating]
        else:
            raw_rating = float(raw_rating)

        user["rating"] = raw_rating

        # ---------- Handle Missing Age ----------
        if user.get("age") is None:
            user["age"] = None

        # ---------- Deduplication ----------
        name = user["name"].strip()

        if name in unique_users:
            continue

        unique_users.add(name)
        cleaned_data.append(user)

    return cleaned_data


# =========================================================
# 3. DATA INSIGHTS FUNCTION
# =========================================================

def get_insights(data):
    """
    Generates meaningful insights from cleaned data.
    - Calculates average rating
    - Counts poor ratings
    """

    if not data:
        print("Dataset is empty")
        return

    total_rating = 0

    for user in data:
        total_rating += float(user["rating"])

    average_rating = total_rating / len(data)
    print("Average Rating:", average_rating)

    # Count poor ratings (< 3)
    poor_ratings = 0

    for user in data:
        if float(user["rating"]) < 3:
            poor_ratings += 1

    poor_percentage = (poor_ratings / len(data)) * 100

    print("Poor Ratings Count:", poor_ratings)
    print("Poor Ratings Percentage:", poor_percentage, "%")


# =========================================================
# 4. RECOMMENDATION SYSTEM (RULE-BASED)
# =========================================================

def get_recommendations(data):
    """
    Recommends a brand based on user rating.
    Rule:
    - Rating >= 4 → Apple
    - Rating < 4 → Samsung
    """

    recommendations = []

    for user in data:
        curr_recommendation = {}

        curr_recommendation["name"] = user["name"]

        if float(user["rating"]) >= 4:
            curr_recommendation["brand"] = "Apple"
        else:
            curr_recommendation["brand"] = "Samsung"

        recommendations.append(curr_recommendation)

    return recommendations


# =========================================================
# 5. MAIN EXECUTION FLOW (OPTIONAL)
# =========================================================

if __name__ == "__main__":
    data = load_data("store_data.json")
    cleaned_data = clean_data(data)

    get_insights(cleaned_data)

    recs = get_recommendations(cleaned_data)
    print("Recommendations:", recs)
