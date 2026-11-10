# ============================================================
# NOTE 03: ETL PIPELINE (DATA MANAGEMENT IN MLOps)
# ============================================================

# --- 1. What is it? ---
# Data Management in MLOps = building pipelines that move data
# from its source to a place where ML models can use it.
# This work is mostly done by the DATA ENGINEER.
# The pipeline is called an ETL pipeline:
#       Extract  ->  Transform  ->  Load

# --- 2. Step 1: EXTRACT (Data Ingestion) ---
# Collect raw data from different sources (apps, APIs, databases).
# Done with: Python, SQL
# Streaming tools: Kafka, Kinesis (for data arriving continuously)