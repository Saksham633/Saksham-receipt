import streamlit as st
import shelve
from fpdf import FPDF

st.title("Saksham Receipt System")

# Permanent storage file
db = shelve.open('my_data', writeback=True)

# Session state initialization
if 'data' not in st.session_state:
    st.session_state.data = {"name": "", "zone": "", "ward": ""}

# Inputs
u_id = st.text_input("Enter Unique ID")

# Search/Load logic
if st.button("Search/Load Data"):
    if u_id in db:
        st.session_state.data = db[u_id]
        st.success(f"Data found for ID: {u_id}")
    else:
        st.warning("ID nahi mili. Naya data enter karein aur 'Save' dabaein.")

# Fields
name = st.text_input("Customer Name", value=st.session_state.data['name'])
zone = st.text_input("Zone No", value=st.session_state.data['zone'])
ward = st.text_input("Ward No", value=st.session_state.data['ward'])
amt = st.text_input("Amount Paid")

# Save logic
if st.button("Save Data"):
    db[u_id] = {"name": name, "zone": zone, "ward": ward}
    st.session_state.data = {"name": name, "zone": zone, "ward": ward}
    st.success("Data permanently save ho gaya!")

# PDF Generation
def generate_pdf(u_id, z, w, name, amt):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Payment Receipt", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Unique ID: {u_id}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name} | Zone: {z} | Ward: {w}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {amt}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

if st.button("Generate Receipt"):
    if name:
        pdf_data = generate_pdf(u_id, zone, ward, name, amt)
        st.download_button("Download PDF", pdf_data, "receipt.pdf", "application/pdf")
    else:
        st.error("Pehle data search ya enter karein!")

db.close()
