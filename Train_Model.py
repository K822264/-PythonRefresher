# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Load the dataset
df = pd.read_csv("salaryData.csv")

# Define features and target
X = df[["Age", "Gender", "Education Level", "Job Title", "Years of Experience"]]
y = df["Salary"]

# Categorical columns to encode
categorical_features = ["Gender", "Education Level", "Job Title"]

# Create a preprocessing pipeline for categorical variables
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],
    remainder="passthrough"  # Leave numerical columns as they are
)

# Full pipeline: preprocessing + model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Fit the model
model.fit(X, y)

# Save the model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model.pkl")
