class Vehicle:
    def __init__(self, license_plate):
        """
        Initialize a vehicle with a license plate
        
        Args:
            license_plate (str): The vehicle's license plate number
        """
        self.license_plate = license_plate
    
    def get_license_plate(self):
        """Return the vehicle's license plate number"""
        return self.license_plate