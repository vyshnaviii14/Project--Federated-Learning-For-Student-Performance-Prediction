import streamlit as st

st.set_page_config(
    page_title="Federated Learning Student Performance Prediction",
    layout="wide"
)

st.title("🎓 Federated Learning Student Performance Prediction")

st.markdown("---")

st.subheader("📌 Project Overview")

st.write("""
This project predicts student academic performance using
Machine Learning and Federated Learning concepts.

Features:
- Student Performance Prediction
- Risk Detection
- Prediction History
- Analytics Dashboard
- Privacy Preserving Learning
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Participating Colleges", "3")

with col2:
    st.metric("Privacy Score", "100%")

with col3:
    st.metric("Federated Clients", "3")

st.markdown("---")

st.info(
    "👈 Use the sidebar to access Prediction, Dashboard, Analytics and History."
)