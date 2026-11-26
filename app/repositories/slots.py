class InMemorySlotRepository:
    def __init__(self, slots: list[str]):
        self.slots = slots
        self.bookings : dict[str, str] = {}     # {slot_id:patient_id}

    def is_free(self, slot_id) -> bool:
        return slot_id in self.slots and slot_id not in self.bookings

    def save_booking(self, slot_id: str, patient_id: str) -> None:
        self.bookings[slot_id] = patient_id

    def list_free(self) -> list[str]:
        return [s for s in self.slots if s not in self.bookings]