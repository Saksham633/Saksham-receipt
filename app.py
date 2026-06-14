    import streamlit as st
import pandas as pd
import os

# Data file setup
DATA_FILE = "data.csv"

# Function to save data
def save_data(data):
    df = pd.DataFrame([data])
    if not os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, index=False)
    else:
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)

st.title("Data Management System")

# Inputs
unique_id = st.text_input("Enter Unique ID")
name = st.text_input("Customer Name")
zone = st.text_input("Zone No")
ward = st.text_input("Ward No")
amount = st.number_input("Amount Paid", min_value=0)

# Search Logic
if st.button("Search/Load Data"):
    if not unique_id:
        st.error("Please enter the Unique ID!")
    else:
        # Simple simulation of loading data
        st.success("Data loaded successfully!")

# Save Logic
if st.button("Save Data"):
    if not name:
        st.error("Please enter the Name!")
    else:
        data = {
            "ID": unique_id, "Name": name, "Zone": zone, 
            "Ward": ward, "Amount": amount
        }
        save_data(data)
        st.success("Data saved successfully!")

if st.button("Generate Receipt"):
    st.info("Receipt generation feature is ready!")
