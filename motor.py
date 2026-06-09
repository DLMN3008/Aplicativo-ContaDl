class MotorContable:

    def __init__(self, db):
        self.db = db

    def ejecutar(self, tipo, data):

        reglas = self.db.execute("""
            SELECT id FROM reglas_contables
            WHERE tipo_operacion=%s AND activo=true
        """, (tipo,)).fetchall()

        resultado = []

        for r in reglas:

            detalles = self.db.execute("""
                SELECT cuenta, tipo_movimiento, campo_origen
                FROM reglas_detalle
                WHERE regla_id=%s
            """, (r.id,)).fetchall()

            for d in detalles:

                valor = data.get(d.campo_origen, 0)

                resultado.append({
                    "cuenta": d.cuenta,
                    "debe": valor if d.tipo_movimiento == "DEBE" else 0,
                    "haber": valor if d.tipo_movimiento == "HABER" else 0
                })

        return resultado
