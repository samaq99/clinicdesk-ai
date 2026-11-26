from app.repositories.slots import InMemorySlotRepository

def book_slot(repo: InMemorySlotRepository, slot_id: str, patient_id: str) -> str:
    if not slot_id:
        raise ValueError("No Slot is selected")
    if not repo.is_free(slot_id):
        raise ValueError(f"Slot ID # {slot_id} is not free")
    repo.save_booking(slot_id, patient_id)
    return f"Booked: Slot # {slot_id}"