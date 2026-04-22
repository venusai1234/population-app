import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ─── CONFIG ─────────────────────────────────────────────
st.set_page_config(page_title="Population Intelligence System", layout="wide")

# ─── CUSTOM UI (PRO LEVEL) ─────────────────────────────
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.title {
    font-size:42px;
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
    box-shadow:0 4px 15px rgba(0,0,0,0.4);
}
.green { background: linear-gradient(135deg,#00b09b,#096843); }
.blue { background: linear-gradient(135deg,#2980b9,#6dd5fa); }
.orange { background: linear-gradient(135deg,#f39c12,#f1c40f); }
.red { background: linear-gradient(135deg,#ff4b4b,#c0392b); }
.metric-box {
    background:white;
    padding:15px;
    border-radius:10px;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ─── HEADER ─────────────────────────────────────────────
st.markdown('<div class="title">🌍 World Population Intelligence System</div>', unsafe_allow_html=True)
st.markdown("**Acharya Nagarjuna University | MCA Final Year Project | CHALLA ASHOK**")
st.markdown("---")

# ─── DATA (USE YOUR PROJECT IDEA) ───────────────────────
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Country": ["India","China","USA","Indonesia","Brazil"],
        "2000": [1050,1260,282,211,175],
        "2010": [1230,1340,309,242,195],
        "2020": [1380,1400,331,273,212],
        "2023": [1428,1412,335,277,216]
    })

df = load_data()

# ─── SIDEBAR (LIKE YOUR APP) ───────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    country = st.selectbox("Select Country", df["Country"])
    year = st.selectbox("Select Year", ["2000","2010","2020","2023"])
    st.markdown("---")

row = df[df["Country"] == country].iloc[0]

# ─── CARDS (PRO STYLE) ─────────────────────────────
col1, col2, col3, col4 = st.columns(4)

growth = ((row["2023"] - row["2000"]) / row["2000"]) * 100
future = int(row["2023"] * 1.05)

with col1:
    st.markdown(f'<div class="card green">{country}<br>{row["2023"]}M</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card blue">Growth<br>{growth:.2f}%</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="card orange">Prediction<br>{future}M</div>', unsafe_allow_html=True)

with col4:
    density = row["2023"] / 100
    st.markdown(f'<div class="card red">Density Index<br>{density:.2f}</div>', unsafe_allow_html=True)

# ─── TREND GRAPH (INTERACTIVE) ─────────────────────
st.markdown("---")
st.subheader("📈 Population Trend Analysis")

years = ["2000","2010","2020","2023"]
values = [row[y] for y in years]

fig = px.line(x=years, y=values, markers=True, title="Growth Trend")
st.plotly_chart(fig, use_container_width=True)

# ─── BAR + PIE (ADVANCED) ─────────────────────
col5, col6 = st.columns(2)

with col5:
    st.subheader("📊 Year Comparison")
    fig2 = px.bar(x=years, y=values, color=values)
    st.plotly_chart(fig2, use_container_width=True)

with col6:
    st.subheader("🌍 Population Share")
    fig3 = px.pie(df, values=year, names="Country", title="Global Share")
    st.plotly_chart(fig3, use_container_width=True)

# ─── HEATMAP (PRO) ─────────────────────
st.markdown("---")
st.subheader("🔥 Heatmap Analysis")

heat = px.imshow(df.set_index("Country"), text_auto=True, color_continuous_scale="RdYlGn")
st.plotly_chart(heat, use_container_width=True)

# ─── SMART INSIGHTS ─────────────────────
st.markdown("---")
st.subheader("💡 Smart Insights")

highest = df.loc[df["2023"].idxmax(), "Country"]

st.info(f"🌍 Highest Population Country: {highest}")

if growth > 30:
    st.success("📈 Rapid Growth Detected")
else:
    st.warning("⚠️ Moderate Growth")

# ─── ADVANCED ANALYTICS ─────────────────────
st.markdown("---")
st.subheader("📊 Advanced Analysis")

df["Growth"] = ((df["2023"] - df["2000"]) / df["2000"]) * 100

fig4 = px.scatter(df, x="Growth", y="2023", size="2023", color="Country",
                  title="Growth vs Population")
st.plotly_chart(fig4, use_container_width=True)

# ─── TABLE ─────────────────────
st.markdown("---")
st.subheader("📋 Dataset")
st.dataframe(df, use_container_width=True)

# ─── FOOTER ─────────────────────
st.markdown("---")
st.markdown("<center>🌍 Population Intelligence System | CHALLA ASHOK | MCA Project</center>", unsafe_allow_html=True)
