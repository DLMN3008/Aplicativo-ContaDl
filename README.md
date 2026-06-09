# Aplicativo-ContaDl
Aplicativo Contable DL Consultoria
# ERP Contable Perú

Motor contable parametrizable con FastAPI + Streamlit.

## 1. Crear base de datos
Ejecutar db/schema.sql en PostgreSQL

## 2. Levantar API
uvicorn api.main:app --reload

## 3. Levantar UI
streamlit run ui/app.py
