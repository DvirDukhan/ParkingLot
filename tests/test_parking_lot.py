import pytest
from src.models.parking_lot import ParkingLot

class TestParkingLot:
    def test_parking_lot_creation(self):
        """Test that a parking lot can be created with a name"""
        name = "Test Parking Lot"
        parking_lot = ParkingLot(name)
        
        assert parking_lot.name == name