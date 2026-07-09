import streamlit as st
import pandas as pd
import os

st.title("📜 Prediction History")

if os.path.exists("predictions.csv"):

    df = pd.read_csv("predictions.csv")

    st.dataframe(df, use_container_width=True)

    st.download_button(
        label="📥 Download Prediction Report",
        data=df.to_csv(index=False),
        file_name="Prediction_Report.csv",
        mime="text/csv"
    )

else:
    st.warning("No predictions available yet.")