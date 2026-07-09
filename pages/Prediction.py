import streamlit as st
import pandas as pd
import os

st.title("🎯 Student Prediction")

college = st.selectbox(
    "Select College",
    ["CollegeA", "CollegeB", "CollegeC"]
)

study_hours = st.number_input(
    "Study Hours",
    min_value=0,
    max_value=15,
    value=5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=5
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0,
    max_value=100,
    value=60
)

if st.button("Predict"):

    predicted_marks = (
        study_hours * 5
        + attendance * 0.3
        + assignments * 2
        + previous_marks * 0.4
    )

    predicted_marks = min(predicted_marks, 100)

    # Risk Level
    if predicted_marks >= 80:
        risk = "Low"
        status = "🟢 Safe Student"

    elif predicted_marks >= 50:
        risk = "Medium"
        status = "🟡 Needs Monitoring"

    else:
        risk = "High"
        status = "🔴 At Risk Student"

    # Performance Level
    if predicted_marks >= 80:
        performance = "Excellent 🏆"

    elif predicted_marks >= 50:
        performance = "Average 👍"

    else:
        performance = "Needs Improvement ⚠️"

    # Results
    st.success(f"Predicted Marks = {predicted_marks:.2f}")

    st.subheader("📊 Risk Score")
    st.progress(int(predicted_marks))
    st.write(f"Score: {predicted_marks:.0f}/100")

    st.success(f"Performance Level = {performance}")
    st.info(f"Risk Level = {risk}")
    st.warning(f"Student Status = {status}")

    # Student Status
    st.subheader("📊 Student Status")

    if risk == "Low":
        st.success("Student is performing well.")
    elif risk == "Medium":
        st.warning("Student needs regular monitoring.")
    else:
        st.error("Immediate intervention required.")

    # AI Recommendations
    st.subheader("📋 AI Recommendations")

    recommendations = []

    if attendance < 75:
        recommendations.append("Improve attendance above 75%")

    if study_hours < 3:
        recommendations.append("Increase study hours")

    if assignments < 5:
        recommendations.append("Complete pending assignments")

    if previous_marks < 50:
        recommendations.append("Focus on weak subjects")

    if predicted_marks >= 80:
        recommendations.append("Maintain current performance level")

    if len(recommendations) == 0:
        recommendations.append("Keep up the good work!")

    for rec in recommendations:
        st.write("✅", rec)

    # Save Prediction
    new_data = pd.DataFrame({
        "College": [college],
        "Marks": [round(predicted_marks, 2)],
        "Risk": [risk]
    })

    if os.path.exists("predictions.csv"):
        old = pd.read_csv("predictions.csv")
        updated = pd.concat([old, new_data], ignore_index=True)
        updated.to_csv("predictions.csv", index=False)
    else:
        new_data.to_csv("predictions.csv", index=False)

    st.success("Prediction Saved Successfully ✅")