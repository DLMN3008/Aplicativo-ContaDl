import streamlit as st
import requests

st.title("ERP Contable Perú")

tipo = st.selectbox("Operación", ["VENTA", "COMPRA"])

subtotal = st.number_input("Subtotal")
igv = st.number_input("IGV")
total = st.number_input("Total")

if st.button("Procesar"):

    r = requests.post(
        f"http://localhost:8000/operacion/{tipo}",
        json={
            "subtotal": subtotal,
            "igv": igv,
            "total": total
        }
    )

    st.json(r.json())
