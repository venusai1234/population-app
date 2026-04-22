import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="🌍 Population Intelligence System", layout="wide")

st.title("🌍 World Population Intelligence System")
st.markdown("### MCA Project - Interactive Dashboard")

# Data
data = {
    "Country": ["India", "China", "USA", "Indonesia", "Brazil"],
    "2000": [1050, 1260, 282, 211, 175],
    "2010": [1230, 1340, 309, 242, 195],
    "2020": [1380, 1400, 331, 273, 212],
    "2023": [1428, 1412, 335, 277, 216]
}

df = pd.DataFrame(data)

# Sidebar
st.sidebar.header("Select Country")
country = st.sidebar.selectbox("Country", df["Country"])

row = df[df["Country"] == country].iloc[0]

# Main
col1, col2 = st.columns(2)

with col1:
    st.subheader("Population Overview")
    st.success(f"{country} Population (2023): {row['2023']} Million")

with col2:
    growth = ((row["2023"] - row["2000"]) / row["2000"]) * 100
    st.metric("Growth %", f"{growth:.2f}%")

# Graph
st.subheader("Population Trend")
years = ["2000", "2010", "2020", "2023"]
values = [row[y] for y in years]

fig, ax = plt.subplots()
ax.plot(years, values, marker='o')
st.pyplot(fig)

# Heatmap
st.subheader("Heatmap")
sns.heatmap(df.set_index("Country"), annot=True)
st.pyplot()

# Table
st.subheader("Dataset")
st.dataframe(df)
