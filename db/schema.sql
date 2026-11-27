CREATE TABLE IF NOT EXISTS bookings(
    id  SERIAL PRIMARY KEY,
    slot_id TEXT NOT NULL UNIQUE,
    patient_id TEXT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);