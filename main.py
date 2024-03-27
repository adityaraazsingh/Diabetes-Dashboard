import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("C:\\Users\\adity\\Documents\\-PRIORITY-\\Diabetes Dashboard\\diabetes.csv")
# Set page title and layout
st.set_page_config(page_title="Diabetes Dashboard", layout="wide")

# Sidebar
st.sidebar.title("Scatter Plot Options")

# Select attributes for scatter plot
x_attribute = st.sidebar.selectbox("Select X-axis attribute", df.columns)
y_attribute = st.sidebar.selectbox("Select Y-axis attribute", df.columns)

# Create scatter plot based on user-selected attributes
st.title("Diabetes Dashboard")
st.subheader("Custom Scatter Plot")

fig, ax = plt.subplots()
colors = df['Outcome'].map({0: 'blue', 1: 'red'})
df.plot(kind='scatter', x=x_attribute, y=y_attribute, c=colors, ax=ax)
plt.xlabel(x_attribute)
plt.ylabel(y_attribute)
st.pyplot(fig)

# Dataset
st.subheader("Dataset")
st.write(df)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Adi")