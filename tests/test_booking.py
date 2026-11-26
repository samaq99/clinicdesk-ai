import pytest
from app.repositories.slots import InMemorySlotRepository
from app.services.booking import book_slot

def test_book_free_slot():
    repo = InMemorySlotRepository(["mon-09", "mon-10"])
    assert book_slot(repo, "mon-09", "p1") == "Booked: Slot # mon-09"

    assert repo.list_free() == ["mon-10"]

def test_second_booking_is_refused():
    repo = InMemorySlotRepository(["mon-09"])
    book_slot(repo, "mon-09", "p1")
    with pytest.raises(ValueError):
        book_slot(repo, "mon-09", "p2")
