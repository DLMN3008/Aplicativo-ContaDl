CREATE TABLE reglas_contables (
    id SERIAL PRIMARY KEY,
    tipo_operacion VARCHAR(50),
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE reglas_detalle (
    id SERIAL PRIMARY KEY,
    regla_id INTEGER,
    cuenta VARCHAR(20),
    tipo_movimiento VARCHAR(10),
    campo_origen VARCHAR(50)
);

CREATE TABLE asientos (
    id SERIAL PRIMARY KEY,
    fecha TIMESTAMP DEFAULT NOW(),
    glosa TEXT
);

CREATE TABLE detalle_asientos (
    id SERIAL PRIMARY KEY,
    asiento_id INTEGER,
    cuenta VARCHAR(20),
    debe NUMERIC,
    haber NUMERIC
);
