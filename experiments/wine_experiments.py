# Based on: scikit-learn official tutorial

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report

wine = load_wine(as_frame=True)
X, y = wine.data, wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Experiment 1: SVM (linear)
clf1 = SVC(kernel='linear')
clf1.fit(X_train, y_train)
print("Experiment 1 - SVM (Linear)")
print(classification_report(y_test, clf1.predict(X_test)))

# Experiment 2: SVM (RBF kernel with scaling)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
clf2 = SVC(kernel='rbf')
clf2.fit(X_train_scaled, y_train)
print("Experiment 2 - SVM (RBF with Scaling)")
print(classification_report(y_test, clf2.predict(X_test_scaled)))

# Experiment 3: Random Forest
clf3 = RandomForestClassifier(n_estimators=100, random_state=42)
clf3.fit(X_train, y_train)
print("Experiment 3 - Random Forest")
print(classification_report(y_test, clf3.predict(X_test)))
