
# Based on: Hands-On ML with Scikit-Learn by Aurélien Géron

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load and split data
iris = load_iris(as_frame=True)
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Experiment 1: Logistic Regression (baseline)
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
print("Experiment 1 - Logistic Regression (No Scaling)")
print(classification_report(y_test, lr.predict(X_test)))

# Experiment 2: Logistic Regression with scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
lr_scaled = LogisticRegression(max_iter=200)
lr_scaled.fit(X_train_scaled, y_train)
print("Experiment 2 - Logistic Regression (With Scaling)")
print(classification_report(y_test, lr_scaled.predict(X_test_scaled)))

# Experiment 3: Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
print("Experiment 3 - Random Forest")
print(classification_report(y_test, rf.predict(X_test)))
