import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

st.write("## Upload your CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("### Data Preview")
    st.dataframe(df.head())

    st.write("## Data Statistics")
    st.write(df.describe())

    st.subheader("### Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value to filter by", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered Data")
    st.dataframe(filtered_df)

    st.subheader("### Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        if filtered_df.empty:
            st.write("No data available for the selected filter.")
        elif not pd.api.types.is_numeric_dtype(filtered_df[x_column]) or not pd.api.types.is_numeric_dtype(filtered_df[y_column]):
            st.write("Selected columns for X or Y axis must contain numeric data.")
        else:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Please upload a CSV file to proceed.")