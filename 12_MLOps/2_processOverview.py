# ============================================================
# NOTE 02: BUILDING AN ML PROJECT USING MLOps (OVERVIEW)
# ============================================================

# --- 1. Example project ---
# YouTube Comment Sentiment Analyzer (multiclass classification).
# Output shown to the user:
#   - total comments, unique comments, average comment length
#   - average sentiment score, pie chart
#   - top 25 comments, detailed analysis
# Delivered as: Chrome plugin (frontend) + Flask API (backend)
# --- 2. High-level flow (runtime) ---
# 1) User uses the frontend (HTML, CSS, JavaScript)
# 2) Frontend sends the request to the Backend API (Flask)
# 3) Backend passes the data to the model
# 4) Model returns the prediction -> backend -> frontend -> user