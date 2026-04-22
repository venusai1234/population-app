import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Population Intelligence System", layout="wide")

# ─── UI ─────────────────────────────
st.markdown("""
<style>
.title { font-size:42px; font-weight:bold; color:white; }
.card {
    padding:20px; border-radius:15px; color:white;
    text-align:center; font-size:20px; font-weight:bold;
}
.green { background: linear-gradient(135deg,#00b09b,#096843); }
.blue { background: linear-gradient(135deg,#2980b9,#6dd5fa); }
.orange { background: linear-gradient(135deg,#f39c12,#f1c40f); }
.result-box {
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}
.success { background: linear-gradient(135deg,#00b09b,#096843); color:white; }
.info { background: linear-gradient(135deg,#2980b9,#6dd5fa); color:white; }
</style>
""", unsafe_allow_html=True)

# ─── HEADER ─────────────────────────────
st.markdown('<div class="title">🌍 World Population Intelligence System</div>', unsafe_allow_html=True)
st.markdown("**Acharya Nagarjuna University | MCA Final Year Project | CHALLA ASHOK**")
st.markdown("---")

# ─── DATA ─────────────────────────────
df = pd.DataFrame({
    "Country": ["India","China","USA","Indonesia","Brazil"],
    "2000": [1050,1260,282,211,175],
    "2010": [1230,1340,309,242,195],
    "2020": [1380,1400,331,273,212],
    "2023": [1428,1412,335,277,216]
})

# ─── SIDEBAR ─────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    country = st.selectbox("Select Country", df["Country"])
    year = st.selectbox("Select Year", ["2000","2010","2020","2023"])
    predict = st.button("🚀 Predict Population")

row = df[df["Country"] == country].iloc[0]

# ─── RESULT SECTION ─────────────────────────────
st.markdown("## 🎯 Prediction Result")

if predict:
    population = row[year]

    if population > 1000:
        style = "success"
        msg = "High Population Country 🌍"
    else:
        style = "info"
        msg = "Moderate Population Country"

    st.markdown(f"""
    <div class="result-box {style}">
    {country} Population in {year} <br><br>
    {population} Million <br><br>
    {msg}
    </div>
    """, unsafe_allow_html=True)

# ─── CARDS ─────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns(3)

growth = ((row["2023"] - row["2000"]) / row["2000"]) * 100
future = int(row["2023"] * 1.05)

with col1:
    st.markdown(f'<div class="card green">{country}<br>{row["2023"]}M</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card blue">Growth<br>{growth:.2f}%</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="card orange">2025 Prediction<br>{future}M</div>', unsafe_allow_html=True)

# ─── GRAPH ─────────────────────────────
st.markdown("---")
st.subheader("📈 Population Trend")

years = ["2000","2010","2020","2023"]
values = [row[y] for y in years]

fig = px.line(x=years, y=values, markers=True)
st.plotly_chart(fig, use_container_width=True)

# ─── PIE ─────────────────────────────
st.subheader("🌍 Global Share")
fig2 = px.pie(df, values="2023", names="Country")
st.plotly_chart(fig2, use_container_width=True)

# ─── INSIGHTS ─────────────────────────────
st.markdown("---")
st.subheader("💡 Insights")

highest = df.loc[df["2023"].idxmax(), "Country"]
st.info(f"🌍 Highest Population Country: {highest}")

if growth > 30:
    st.success("📈 Rapid Growth")
else:
    st.warning("⚠️ Moderate Growth")

# ─── TABLE ─────────────────────────────
st.markdown("---")
st.subheader("📋 Dataset")
st.dataframe(df, use_container_width=True)

# ─── FOOTER ─────────────────────────────
st.markdown("---")
st.markdown("<center>🌍 Population Intelligence System | CHALLA ASHOK</center>", unsafe_allow_html=True)
