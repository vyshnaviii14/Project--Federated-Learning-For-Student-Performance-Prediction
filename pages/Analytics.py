import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📈 Analytics")

if not os.path.exists("predictions.csv"):
    st.warning("No predictions available yet.")
    st.stop()

df = pd.read_csv("predictions.csv")

# College Filter
st.subheader("🎓 Filter Data")

selected_college = st.selectbox(
    "Select College",
    ["All"] + list(df["College"].unique())
)

if selected_college != "All":
    df = df[df["College"] == selected_college]

# Risk Distribution
st.subheader("🎯 Risk Distribution")

risk_counts = df["Risk"].value_counts().reset_index()
risk_counts.columns = ["Risk", "Count"]

fig1 = px.pie(
    risk_counts,
    values="Count",
    names="Risk",
    title="Risk Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# College Performance
st.subheader("🏫 College Wise Performance")

college_avg = df.groupby("College")["Marks"].mean().reset_index()

fig2 = px.bar(
    college_avg,
    x="College",
    y="Marks",
    title="Average Marks by College",
    text_auto=".2f"
)

st.plotly_chart(fig2, use_container_width=True)

# Prediction Trend
st.subheader("📈 Prediction Trend")

df["Student"] = range(1, len(df) + 1)

fig3 = px.line(
    df,
    x="Student",
    y="Marks",
    markers=True,
    title="Prediction Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# Summary Metrics
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Predictions", len(df))

with col2:
    st.metric("Average Marks", round(df["Marks"].mean(), 2))

with col3:
    st.metric(
        "High Risk Students",
        len(df[df["Risk"] == "High"])
    )

# Dataset
st.subheader("📋 Prediction Dataset")

st.dataframe(df, use_container_width=True)