import pytest
from src.models.parking_spot import ParkingSpot

class TestParkingSpot:
    def test_parking_spot_creation(self):
        """Test that a parking spot can be created with an ID"""
        spot_id = 123
        spot = ParkingSpot(spot_id)
        
        assert spot.spot_id == spot_id