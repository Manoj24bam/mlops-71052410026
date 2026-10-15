import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Generate sample student data
np.random.seed(42)
n_samples = 200
study_hours = np.random.uniform(1, 10, n_samples)
attendance = np.random.uniform(40, 100, n_samples)
internal_marks = np.random.uniform(10, 50, n_samples)

# Rule for Pass (1) or Fail (0): weighted score threshold
score = (study_hours * 2) + (attendance * 0.4) + (internal_marks * 0.8)
pass_fail = (score > 65).astype(int)

df = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'internal_marks': internal_marks,
    'pass_fail': pass_fail
})

# 2. Train model
X = df[['study_hours', 'attendance', 'internal_marks']]
y = df['pass_fail']

model = LogisticRegression()
model.fit(X, y)

# 3. Save model
joblib.dump(model, 'model.pkl')
print("Model trained and saved successfully.")
