import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Real Estate Analysis Tool", layout="wide")

# Title
st.title("Real Estate Analysis Tool")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)
    
    # Show raw data
    st.subheader("Raw Data")
    st.write(data)
    
    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(data.describe())
    
    # Show data columns
    st.subheader("Data Columns")
    st.write(data.columns)
    
    # Select columns for analysis
    st.subheader("Select Columns for Analysis")
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
    
    x_axis = st.selectbox("Select X-axis Column", options=numerical_columns)
    y_axis = st.selectbox("Select Y-axis Column", options=numerical_columns)
    hue = st.selectbox("Select Hue Column", options=categorical_columns + [None])
    
    # Plotting
    st.subheader("Data Visualization")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)
    plt.title(f"{y_axis} vs {x_axis}")
    st.pyplot(fig)
    
    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    corr_matrix = data.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
    # Additional analysis
    st.subheader("Additional Analysis")
    selected_column = st.selectbox("Select Column for Additional Analysis", options=numerical_columns)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data[selected_column], kde=True, ax=ax)
    plt.title(f"Distribution of {selected_column}")
    st.pyplot(fig)
else:
    st.write("Please upload a CSV file to get started.")

# Footer
st.write("---")
st.write("Real Estate Analysis Tool by [Your Name]")
