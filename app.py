import streamlit as st
from datetime import datetime, timedelta

st.title("Saksham Receipt Generator")

trans_id = st.text_input("Transaction ID")
unique_id = st.text_input("Unique ID")
zone_no = st.text_input("Zone No")
ward_no = st.text_input("Ward No")
customer_name = st.text_input("Customer Name")
amount = st.text_input("Amount Paid")

if st.button("Generate Receipt"):
    now = datetime.utcnow() + timedelta(hours=5, minutes=30)
    st.text("--- SAKSHAM NAGAR NIGAM ---")
    st.text("BAREILLY")
    st.text("HelpLine No:7500240628")
    st.text(f"Trans Date: {now.strftime('%d-%b-%Y %H:%M:%S')}")
    st.text(f"Trans No: {trans_id}")
    st.text(f"Unique Id: {unique_id}")
    st.text(f"Zone No: {zone_no}")
    st.text(f"Ward No: {ward_no}")
    st.text(f"Customer: {customer_name}")
    st.text(f"Month: {now.strftime('%b%Y').upper()}")
    st.text(f"Amount: {amount}")
    st.text("***************************")
  
