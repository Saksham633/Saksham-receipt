import streamlit as st
import pandas as pd
import os

# CSV file ka naam
DATA_FILE = "student_data.csv"

st.title("Saksham Receipt System")

# Form inputs
name = st.text_input("Customer Name")
unique_id = st.text_input("Enter Unique ID")
zone = st.text_input("Zone No")
ward = st.text_input("Ward No")
amount = st.number_input("Amount Paid", min_value=0)

if st.button("Save Data"):
    if not name:
        st.error("Please enter the Name!")
    else:
        # Data ko dictionary mein store kiya
        new_data = pd.DataFrame([{
            "ID": unique_id, "Name": name, 
            "Zone": zone, "Ward": ward, "Amount": amount
        }])
        
        # CSV file mein save/append kiya
        if not os.path.exists(DATA_FILE):
            new_data.to_csv(DATA_FILE, index=False)
        else:
            new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
            
        st.success("Data saved successfully!")

# Records dekhne ke liye
if st.checkbox("View All Records"):
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        st.write(df)
        
