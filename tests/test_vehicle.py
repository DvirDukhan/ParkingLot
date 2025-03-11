import pytest
from src.models.vehicle import Vehicle

class TestVehicle:
    def test_vehicle_creation(self):
        """Test that a vehicle can be created with a license plate"""
        license_plate = "ABC123"
        vehicle = Vehicle(license_plate)
        
        assert vehicle.get_license_plate() == license_plate