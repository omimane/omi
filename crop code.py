# Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from scipy.stats import ttest_ind
import plotly.express as px
import plotly.graph_objects as go
import os

# Create output folder for plots
os.makedirs("plots", exist_ok=True)

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("Crop_recommendation.csv")

# Label Encoding
le = LabelEncoder()
df['label_encoded'] = le.fit_transform(df['label'])

# -----------------------------
# 2. Pie Chart – Crop Distribution
# -----------------------------
crop_counts = df['label'].value_counts()
fig_pie = px.pie(values=crop_counts.values, names=crop_counts.index, title="Crop Distribution")
fig_pie.write_html("plots/pie_chart.html")
print("✅ Pie chart saved to plots/pie_chart.html")

# -----------------------------
# 3. Data Overview
# -----------------------------
print("🔍 Data Overview:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 4. Boxplots for Outlier Detection
# -----------------------------
numerical_cols = df.select_dtypes(include=np.number).columns.drop('label_encoded')

for col in numerical_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Outlier Detection - {col}")
    plt.savefig(f"plots/boxplot_{col}.png")
    plt.close()

# -----------------------------
# 5. Line + Dot Graph for Selected Crops
# -----------------------------
sample_crops = df[df['label'].isin(['rice', 'maize', 'mungbean'])]

for feature in ['N', 'P', 'K']:
    plt.figure(figsize=(8, 4))
    for crop in sample_crops['label'].unique():
        subset = sample_crops[sample_crops['label'] == crop]
        plt.plot(subset[feature].values, marker='o', label=crop)
    plt.title(f'{feature} Levels for Selected Crops')
    plt.xlabel('Sample Index')
    plt.ylabel(feature)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"plots/line_dot_{feature}.png")
    plt.close()

# -----------------------------
# 6. Histograms for Distribution
# -----------------------------
for col in numerical_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"plots/hist_{col}.png")
    plt.close()

# -----------------------------
# 7. Chi-Square Feature Selection
# -----------------------------
X = df[numerical_cols]
y = df['label_encoded']

selector = SelectKBest(score_func=chi2, k='all')
X_new = selector.fit_transform(X, y)
scores = pd.DataFrame({'Feature': X.columns, 'Score': selector.scores_})
print("\n📊 Chi-Square Feature Scores:")
print(scores.sort_values(by="Score", ascending=False))

# -----------------------------
# 8. Funnel Chart – Feature Flow
# -----------------------------
funnel_stages = ["Original Features", "Chi2 Selected", "Used in Model"]
funnel_values = [len(X.columns), 7, 7]  # Adjust as per selection logic
fig_funnel = go.Figure(go.Funnel(
    y=funnel_stages,
    x=funnel_values,
    textinfo="value+percent initial"
))
fig_funnel.update_layout(title="Feature Selection Funnel")
fig_funnel.write_html("plots/funnel_chart.html")
print("✅ Funnel chart saved to plots/funnel_chart.html")

# -----------------------------
# 9. Statistical T-Tests
# -----------------------------
print("\n🧪 T-Test Between First Two Crop Classes:")
class_0 = df[df['label'] == df['label'].unique()[0]]
class_1 = df[df['label'] == df['label'].unique()[1]]

for col in numerical_cols:
    stat, p = ttest_ind(class_0[col], class_1[col])
    print(f"{col}: p-value = {p:.4f}")

# -----------------------------
# 10. Train Random Forest Model
# -----------------------------
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# -----------------------------
# 11. Evaluation
# -----------------------------
y_pred = pipeline.predict(X_test)
print("\n📈 Model Evaluation:")
print(classification_report(y_test, y_pred))
print("✅ Accuracy Score:", accuracy_score(y_test, y_pred))
