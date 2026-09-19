-- Synthetic products only. Prices use whole TWD to keep this exercise small.
CREATE TABLE IF NOT EXISTS week04_products (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price_twd INTEGER NOT NULL CHECK (price_twd >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0)
);
