import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="🌍 Population Intelligence System", layout="wide")

st.markdown("""
<style>
    .main-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    .metric-box {
        background: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    data = {
        "Country": ["India", "China", "USA", "Indonesia", "Brazil"],
        "2000": [1050, 1260, 282, 211, 175],
        "2010": [1230, 1340, 309, 242, 195],
        "2020": [1380, 1400, 331, 273, 212],
        "2023": [1428, 1412, 335, 277, 216]
    }
    return pd.DataFrame(data)

df = load_data()

st.markdown("# 🌍 World Population Intelligence System")
st.markdown("**MCA Final Year Project | Interactive Dashboard**")
st.markdown("---")

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    country = st.selectbox("Select Country", df["Country"])
    st.markdown("---")

row = df[df["Country"] == country].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🌍 Population Overview")

    st.markdown(f"""
    <div class="main-card">
    {country} Population (2023)<br>
    {row['2023']} Million
    </div>
    """, unsafe_allow_html=True)

    growth = ((row["2023"] - row["2000"]) / row["2000"]) * 100
    st.markdown("<br>", unsafe_allow_html=True)
    st.metric("📈 Growth (2000-2023)", f"{growth:.2f}%")

with col2:
    st.markdown("## 📊 Key Metrics")
    cols = st.columns(3)
    cols[0].metric("2000", f"{row['2000']}M")
    cols[1].metric("2010", f"{row['2010']}M")
    cols[2].metric("2020", f"{row['2020']}M")

st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.markdown("## 📈 Population Trend")
    years = ["2000", "2010", "2020", "2023"]
    values = [row[y] for y in years]

    fig, ax = plt.subplots()
    ax.plot(years, values, marker='o', linewidth=3)
    ax.set_title("Population Growth")
    ax.set_ylabel("Millions")
    st.pyplot(fig)

with col4:
    st.markdown("## 📊 Comparison")
    fig2, ax2 = plt.subplots()
    ax2.bar(years, values)
    ax2.set_title("Year-wise Population")
    st.pyplot(fig2)

st.markdown("---")
st.markdown("## 🔥 Population Heatmap")

heat_data = df.set_index("Country")
fig3, ax3 = plt.subplots()
sns.heatmap(heat_data, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

st.markdown("---")
st.markdown("## 🔮 Future Prediction")

future = int(row["2023"] * 1.05)
st.success(f"Estimated Population (2025): {future} Million")

st.markdown("---")
st.markdown("## 📋 Dataset")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("<center><small>🌍 Population Intelligence System | MCA Project</small></center>", unsafe_allow_html=True)
