import streamlit as st
import random
from fpdf import FPDF
from datetime import datetime

st.title("Saksham Receipt System")

# 1. Hamara Data (Aap yahan aur IDs add kar sakte hain)
database = {
    "1001": {"name": "Abhishek", "zone": "1", "ward": "5"},
    "1002": {"name": "Saksham", "zone": "2", "ward": "8"}
}

# 2. Session State ka use (Data page refresh par nahi jayega)
if 'random_id' not in st.session_state: st.session_state.random_id = ""
if 'data' not in st.session_state: st.session_state.data = {"name": "", "zone": "", "ward": ""}

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Generate New Random ID"):
        st.session_state.random_id = str(random.randint(1000, 9999))
        st.session_state.data = {"name": "", "zone": "", "ward": ""}

# Inputs
unique_id = st.text_input("Unique ID", value=st.session_state.random_id)

if st.button("Search Data"):
    if unique_id in database:
        st.session_state.data = database[unique_id]
        st.success("Data Found!")
    else:
        st.error("ID not found in database!")

# Form Fields (Jo auto-fill honge)
name = st.text_input("Customer Name", value=st.session_state.data['name'])
zone = st.text_input("Zone No", value=st.session_state.data['zone'])
ward = st.text_input("Ward No", value=st.session_state.data['ward'])
amt = st.text_input("Amount Paid")

# PDF Function
def generate_pdf(u_id, z, w, name, amt):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Payment Receipt", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Unique ID: {u_id}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name} | Zone: {z} | Ward: {w}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {amt}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# Generate Receipt
if st.button("Generate Receipt"):
    if name:
        pdf_data = generate_pdf(unique_id, zone, ward, name, amt)
        st.download_button("Download PDF", pdf_data, "receipt.pdf", "application/pdf")
    else:
        st.warning("Please search for a valid ID first!")
        
