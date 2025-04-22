import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import base64

# -----------------------------
# 1. Page Config
# -----------------------------
st.set_page_config(page_title="🌾 Crop Recommendation", layout="centered")

# -----------------------------
# 2. Hero Background Section
# -----------------------------
def set_hero_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <style>
        .hero {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            height: 25vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
            border-radius: 0 0 15px 15px;
        }}
        .content {{
            margin-top: 30px;
            padding: 30px;
            border-radius: 15px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            font-weight: bold;
        }}
        .stSlider > div {{
            padding-top: 10px;
            padding-bottom: 10px;
        }}
        </style>
        <div class='hero'>🌾 Crop Recommendation</div>
    """, unsafe_allow_html=True)

set_hero_background("background.jpg")  # Or background.png

# -----------------------------
# 3. Load and Train Model
# -----------------------------
@st.cache_data
def train_model():
    df = pd.read_csv("Crop_recommendation.csv")
    X = df.drop("label", axis=1)
    y = LabelEncoder().fit_transform(df["label"])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = RandomForestClassifier()
    model.fit(X_scaled, y)
    label_map = dict(zip(range(len(np.unique(df["label"]))), sorted(df["label"].unique())))
    return model, scaler, label_map

model, scaler, label_mapping = train_model()

# -----------------------------
# 4. Crop Recommendation Form
# -----------------------------
st.markdown("<div class='content'>", unsafe_allow_html=True)

st.markdown("### 💡 Enter soil and climate details below:")

N = st.slider("Nitrogen (N)", 0, 140, 50)
P = st.slider("Phosphorus (P)", 5, 145, 50)
K = st.slider("Potassium (K)", 5, 205, 50)
temperature = st.slider("Temperature (°C)", 8, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 60)
ph = st.slider("Soil pH", 3.5, 9.5, 6.5)
rainfall = st.slider("Rainfall (mm)", 20, 300, 100)

if st.button("🌱 Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)
    crop = label_mapping[prediction[0]]
    st.success(f"✅ Recommended Crop: **{crop.upper()}**")

st.markdown("</div>", unsafe_allow_html=True)
