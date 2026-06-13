import streamlit as st
from fpdf import FPDF
from datetime import datetime, timedelta

st.title("Saksham Receipt Generator")

# Inputs
t_id = st.text_input("Transaction ID")
u_id = st.text_input("Unique ID")
zone = st.text_input("Zone No")
ward = st.text_input("Ward No")
name = st.text_input("Customer Name")
amt = st.text_input("Amount Paid")

# PDF Function
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="SAKSHAM NAGAR NIGAM", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Trans Date: {datetime.utcnow().strftime('%Y-%m-%d')}", ln=True)
    pdf.cell(200, 10, txt=f"Trans No: {t_id}", ln=True)
    pdf.cell(200, 10, txt=f"Unique ID: {u_id}", ln=True)
    pdf.cell(200, 10, txt=f"Zone: {zone} | Ward: {ward}", ln=True)
    pdf.cell(200, 10, txt=f"Customer Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Amount Paid: {amt}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# Button
if st.button("Generate Receipt"):
    pdf_data = generate_pdf()
    st.download_button("Download PDF Receipt", pdf_data, "receipt.pdf", "application/pdf")
    
