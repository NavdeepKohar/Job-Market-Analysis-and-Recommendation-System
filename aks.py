import streamlit as st
import pandas as pd

st.title("Excel File Data Preview")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        # Read Excel file
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")

        st.subheader("Data Preview")
        st.dataframe(df.head())

        # Column selection
        column = st.selectbox("Select a column to inspect", df.columns)

        if column:
            st.subheader(f"Details of Column: {column}")
            st.write("**Data Type:**", df[column].dtype)
            st.write("**Number of Non-Null Values:**", df[column].count())
            st.write("**Number of Null Values:**", df[column].isnull().sum())
            st.write("**Unique Values:**", df[column].nunique())

            if pd.api.types.is_numeric_dtype(df[column]):
                st.write("**Basic Statistics:**")
                st.write(df[column].describe())
            else:
                st.write("**Top 5 Most Frequent Values:**")
                st.write(df[column].value_counts().head())

    except Exception as e:
        st.error(f"Error reading the file: {e}")
