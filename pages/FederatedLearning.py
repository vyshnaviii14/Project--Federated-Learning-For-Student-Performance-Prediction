import streamlit as st
import time

st.title("🌐 Federated Learning Simulation")

st.write("""
This simulation demonstrates how Federated Learning works.

✅ Each college trains its own model locally

✅ Student data never leaves the college

✅ Only model updates are shared

✅ Global model is created by aggregating all local models
""")

if st.button("🚀 Start Federated Training"):

    progress = st.progress(0)

    status = st.empty()

    status.write("🏫 Training Model at College A...")
    progress.progress(25)
    time.sleep(1)

    status.write("🏫 Training Model at College B...")
    progress.progress(50)
    time.sleep(1)

    status.write("🏫 Training Model at College C...")
    progress.progress(75)
    time.sleep(1)

    status.write("🌐 Aggregating Local Models...")
    progress.progress(100)
    time.sleep(1)

    st.success("✅ Global Model Updated Successfully")

    st.subheader("📊 Training Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("College A Accuracy", "84%")

    with col2:
        st.metric("College B Accuracy", "81%")

    with col3:
        st.metric("College C Accuracy", "86%")

    st.metric("🌍 Global Model Accuracy", "89%")

    st.info(
        "Student data was never shared. Only model parameters were aggregated."
    )
    st.code("""
College A
    ↓
College B
    ↓
College C
    ↓
Aggregation Server
    ↓
Global Model
""")