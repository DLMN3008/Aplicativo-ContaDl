import requests
import streamlit as st

st.title("ERP Contable Perú")

tipo = st.selectbox("Operación", ["VENTA", "COMPRA"])

subtotal = st.number_input("Subtotal")
igv = st.number_input("IGV")
total = st.number_input("Total")

if st.button("Procesar"):

    try:
        r = requests.post(
            f"http://127.0.0.1:8000/operacion/{tipo}",
            json={
                "subtotal": subtotal,
                "igv": igv,
                "total": total
            },
            timeout=5
        )

        st.json(r.json())

    except requests.exceptions.ConnectionError:
        st.error("❌ No se pudo conectar con la API. ¿Está corriendo FastAPI?")
