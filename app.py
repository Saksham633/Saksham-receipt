import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import os

# Data file setup
DATA_FILE = "student_fees.csv"

def save_data(data):
    df = pd.DataFrame([data])
    if not os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, index=False)
    else:
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)

st.title("St. Xavier's School - Fee Management")

# Form inputs
name = st.text_input("Student Name")
adm_no = st.text_input("Admission Number")
cls = st.text_input("Class & Section")
amount = st.number_input("Amount Paid", min_value=0)

if st.button("Generate & Save Receipt"):
    data = {
        "Name": name, "Adm": adm_no, "Class": cls, 
        "Amount": amount, "Date": datetime.now().strftime("%Y-%m-%d")
    }
    save_data(data)
    st.success("Data Saved Successfully!")
    
    # PDF Logic
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="ST. XAVIER'S SCHOOL", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Student: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Adm No: {adm_no}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {amount}", ln=True)
    
    pdf_output = pdf.output(dest='S').encode('latin-1')
    st.download_button("Download Receipt", data=pdf_output, file_name="receipt.pdf")

# Admin section to see all data
if st.checkbox("View All Records"):
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        st.write(df)
        
