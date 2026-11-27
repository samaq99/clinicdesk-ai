import psycopg

class PostgresSlotRepository:
    def __init__(self, db_url: str, slots:list[str]):
        self.db_url = db_url
        self.slots = slots

    def is_free(self, slot_id: str) -> bool:
        with psycopg.connect(self.db_url) as conn:
            row = conn.execute("select 1 from bookings where slot_id = %s", (slot_id,)).fetchone()
            return slot_id in self.slots and row is None

    def list_free(self) -> list[str]:
        with psycopg.connect(self.db_url) as conn:
            rows = conn.execute("select slot_id from bookings").fetchall()
            booked = {r[0] for r in rows}
            return [s for s in self.slots if s not in booked]

    def save_booking(self, slot_id: str, patient_id: str) -> None:
        with psycopg.connect(self.db_url) as conn:
            conn.execute("insert into bookings (slot_id, patient_id) values (%s,%s)", (slot_id, patient_id),)
            