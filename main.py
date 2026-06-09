from fastapi import FastAPI, Depends
from api.db import SessionLocal
from motor.motor import MotorContable

app = FastAPI(title="ERP Contable Perú")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/operacion/{tipo}")
def operacion(tipo: str, data: dict, db=Depends(get_db)):

    motor = MotorContable(db)

    asiento = motor.ejecutar(tipo, data)

    return {"asiento": asiento}
