# ============================================================
# NOTE 01: INTRODUCTION TO MLOps
# ============================================================

# --- 1. What is MLOps? ---
# MLOps = Machine Learning + Operations.
# It is the set of practices to take an ML model from a notebook
# to a real, running product, and keep it working reliably.
# Simple idea: DevOps (for normal software) applied to ML.

# --- 2. Why do we need it? ---
# Training a model is only about 10-20% of the work.
# Real-world problems that MLOps solves:
#   - "It works on my laptop" but fails on another machine
#   - Models become outdated over time (data changes)
#   - No one knows which code/data/model version is running
#   - Manual deployment is slow and error-prone

# --- 3. The ML lifecycle (the big picture) ---
# Data collection -> Data prep -> Training -> Evaluation
#   -> Packaging -> Deployment -> Monitoring -> (repeat)
# MLOps covers the whole loop, not just training.

# --- 4. Core building blocks ---
# Version control    : Git (code), DVC (data and models)
# Containerization   : Docker (same environment everywhere)
# CI/CD              : GitHub Actions (auto test + auto deploy)
# Serving            : FastAPI (model behind an API)
# Cloud              : AWS / GCP (where the app actually runs)
# Monitoring         : logs, latency, cost, accuracy over time
# Experiment tracking: MLflow / Weights & Biases