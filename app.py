import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aadhaar Enrollment Dashboard")

uploaded_file = st.file_uploader("Upload the combined CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head(10))

    # Total enrollment per row
    df["total_enrollment"] = (
        df["age_0_5"] +
        df["age_5_17"] +
        df["age_18_greater"]
    )

    # State summary
    state_summary = df.groupby("state")[["age_0_5", "age_5_17", "age_18_greater", "total_enrollment"]].sum()
    st.subheader("State-wise Summary")
    st.dataframe(state_summary)

    # Top 10
    top10 = state_summary.sort_values("total_enrollment", ascending=False).head(10)

    st.subheader("Top 10 States by Total Enrollment")
    st.dataframe(top10)

    # Bar chart
    st.subheader("Top 10 States Chart")

    fig, ax = plt.subplots(figsize=(12,5))
    ax.bar(top10.index, top10["total_enrollment"])
    ax.set_xticklabels(top10.index, rotation=45, ha='right')
    ax.set_ylabel("Total Enrollment")
    st.pyplot(fig)

    st.info("Dashboard generated successfully!")
else:
    st.warning("Please upload the CSV file to continue.")
