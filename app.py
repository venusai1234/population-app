import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="🌍 Population Intelligence System", layout="wide")

# ─── CUSTOM UI ─────────────────────────────
st.markdown("""
<style>
.main-title {
    font-size:40px;
    font-weight:bold;
    color:white;
}
.card {
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:20px;
    font-weight:bold;
    box-shadow:0 4px 15px rgba(0,0,0,0.3);
}
.green { background: linear-gradient(135deg,#00b09b,#096843); }
.blue { background: linear-gradient(135deg,#2980b9,#6dd5fa); }
.orange { background: linear-gradient(135deg,#f39c12,#f1c40f); }
.metric-box {
    background:white;
    padding:15px;
    border-radius:10px;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ─── DATA ─────────────────────────────
data = {
    "Country": ["India", "China", "USA", "Indonesia", "Brazil"],
    "2000": [1050, 1260, 282, 211, 175],
    "2010": [1230, 1340, 309, 242, 195],
    "2020": [1380, 1400, 331, 273, 212],
    "2023": [1428, 1412, 335, 277, 216]
}
df = pd.DataFrame(data)

# ─── HEADER ─────────────────────────────
st.markdown('<p class="main-title">🌍 World Population Intelligence System</p>', unsafe_allow_html=True)
st.markdown("### MCA Project - Interactive Dashboard")
st.markdown("---")

# ─── SIDEBAR ─────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    country = st.selectbox("Select Country", df["Country"])

row = df[df["Country"] == country].iloc[0]

# ─── CARDS ─────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="card green">{country} Population<br>{row["2023"]} Million</div>', unsafe_allow_html=True)

with col2:
    growth = ((row["2023"] - row["2000"]) / row["2000"]) * 100
    st.markdown(f'<div class="card blue">Growth<br>{growth:.2f}%</div>', unsafe_allow_html=True)

with col3:
    future = int(row["2023"] * 1.05)
    st.markdown(f'<div class="card orange">2025 Prediction<br>{future} Million</div>', unsafe_allow_html=True)

# ─── GRAPH SECTION ─────────────────────────────
st.markdown("---")
col4, col5 = st.columns(2)

years = ["2000","2010","2020","2023"]
values = [row[y] for y in years]

with col4:
    st.subheader("📈 Population Trend")
    fig, ax = plt.subplots()
    ax.plot(years, values, marker='o', linewidth=3)
    ax.set_title("Growth Trend")
    st.pyplot(fig)

with col5:
    st.subheader("📊 Year Comparison")
    fig2, ax2 = plt.subplots()
    ax2.bar(years, values)
    st.pyplot(fig2)

# ─── HEATMAP ─────────────────────────────
st.markdown("---")
st.subheader("🔥 Population Heatmap")

fig3, ax3 = plt.subplots()
sns.heatmap(df.set_index("Country"), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# ─── INSIGHTS ─────────────────────────────
st.markdown("---")
st.subheader("💡 Insights")

highest = df.loc[df["2023"].idxmax(), "Country"]
st.info(f"🌍 Highest population country: {highest}")

if growth > 30:
    st.success("📈 Rapid growth detected")
else:
    st.warning("⚠️ Moderate growth")

# ─── TABLE ─────────────────────────────
st.markdown("---")
st.subheader("📋 Dataset")
st.dataframe(df, use_container_width=True)

# ─── FOOTER ─────────────────────────────
st.markdown("---")
st.markdown("<center>🌍 Population Dashboard | MCA Project</center>", unsafe_allow_html=True)
