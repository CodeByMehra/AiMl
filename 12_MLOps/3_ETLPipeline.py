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

# --- 3. Step 2: TRANSFORM (Data Transformation) ---
# Clean and reshape the raw data so it is usable.
# Done with: Python (small/medium data) or Spark (very large data)
# Example work: remove duplicates, fix missing values, change formats

# --- 4. Step 3: LOAD (Data Storage) ---
# Store the processed data. The 5 storage types:
#   Database (SQL)   : structured tables (e.g. MySQL, PostgreSQL)
#   NoSQL database   : flexible, non-table data (e.g. MongoDB)
#   Data Warehouse   : cleaned, structured data for analysis/reports
#   Data Lake        : huge amounts of raw data in any format
#   Object/File store: files such as images, audio, CSV (e.g. S3)
