import streamlit as st
import shelve
import random
from fpdf import FPDF
from datetime import datetime

st.title("Saksham Receipt System")

# Permanent storage
db = shelve.open('my_data', writeback=True)

if 'data' not in st.session_state:
    st.session_state.data = {"name": "", "zone": "", "ward": ""}

if st.button("Generate New Random ID"):
    st.session_state.random_id = str(random.randint(1000, 9999))

u_id = st.text_input("Enter Unique ID", value=st.session_state.get('random_id', ''))

if st.button("Search/Load Data"):
    if u_id in db:
        st.session_state.data = db[u_id]
        st.success("DATA LOAD SUCCESSFULLY!")
    else:
        st.warning("Unique ID not found!")

name = st.text_input("Customer Name", value=st.session_state.data['name'])
zone = st.text_input("Zone No", value=st.session_state.data['zone'])
ward = st.text_input("Ward No", value=st.session_state.data['ward'])
amt = st.text_input("Amount Paid")

if st.button("Save Data"):
    db[u_id] = {"name": name, "zone": zone, "ward": ward}
    st.success("DATA SAVE SUCCESSFULLY!")

# Fixed PDF Function
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="SAKSHAM NAGAR NIGAM", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='R')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Unique ID: {u_id}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Zone: {zone}", ln=True)
    pdf.cell(200, 10, txt=f"Ward: {ward}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {amt}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

if st.button("Generate Receipt"):
    if name:
        pdf_bytes = create_pdf()
        st.download_button(label="Click Here to Download PDF", data=pdf_bytes, file_name="receipt.pdf", mime="application/pdf")
    else:
        st.error("PLEASE ENTER THE NAME!")

db.close()
