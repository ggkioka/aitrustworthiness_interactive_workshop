
# Based on: scikit-learn examples

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

# Load and split data
data = load_breast_cancer(as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Experiment 1: Decision Tree (default)
clf1 = DecisionTreeClassifier(random_state=0)
clf1.fit(X_train, y_train)
print("Experiment 1 - Decision Tree")
print(classification_report(y_test, clf1.predict(X_test)))

# Experiment 2: Decision Tree (limited depth)
clf2 = DecisionTreeClassifier(max_depth=3, random_state=42)
clf2.fit(X_train, y_train)
print("Experiment 2 - Decision Tree (Max Depth = 3)")
print(classification_report(y_test, clf2.predict(X_test)))

# Experiment 3: Gradient Boosting
clf3 = GradientBoostingClassifier(random_state=0)
clf3.fit(X_train, y_train)
print("Experiment 3 - Gradient Boosting")
print(classification_report(y_test, clf3.predict(X_test)))
