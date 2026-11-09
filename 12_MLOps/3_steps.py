# --- 3. The 10 steps ---
# Step 1 : Data
#          - Twitter and Reddit comment datasets (Kaggle)
#          - Choose the best one, apply feature engineering
#          - Handle class imbalance (cleaning techniques)

# Step 2 : Experimentation and experiment tracking
#          - Tool: MLflow (logs params, metrics, models)
# Step 3 : Automation using DVC pipeline
#          - Reproducible stages: data -> train -> evaluate
# Step 4 : Model Registry (MLflow can be used)
#          - Stores versioned, trained models
# Step 5 : Testing and promoting the model
# Step 6 : Developing the Flask API and Chrome plugin frontend
# Step 7 : Dockerization (package app + dependencies)
# Step 8 : Deploy on AWS EC2
# Step 9 : Deployment strategies
# Step 10: CI/CD pipeline (automatic test + deploy)

# --- 4. Model lifecycle (from the Step 6 slide) ---
# Experiments --(param values)--> DVC Pipeline
#   --(trained model)--> Model Registry
#   --(staging)--> Testing
#   --(production)--> model served by the Backend API
# Idea: a model only reaches production after passing staging tests.

# --- 5. Improvements (next level) ---
# a) Monitoring -> track the app -> Prometheus / Grafana
# b) Retraining loop (retrain when data/performance drifts)
# Tool upgrades (simple tool -> advanced tool):
#   MLflow        -> Weights & Biases (W&B)
#   DVC pipeline  -> Airflow / Kubeflow
#   ASG (Auto Scaling Group, as I read it) -> Kubernetes
#   AWS           -> GCP / Azure
# Many of these together -> AWS SageMaker (all-in-one platform)

# --- 6. One-line summary ---
# Data -> Experiment -> Automate -> Register -> Test -> API
#   -> Docker -> Deploy -> Strategy -> CI/CD -> Monitor -> Retrain