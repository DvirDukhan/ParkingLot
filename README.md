# Parking Lot System

This project is a skeleton implementation of a parking lot system designed for QA engineer interviews. The system simulates a parking lot with different types of parking spots and vehicles.

## Core Components

### Vehicle
- Has license plate and size (S/M/L/XL)
- Types: Compact, Sedan, SUV, Pickup

### Parking Spot
- Has a number (ID), status (free/occupied), and size (Small/Big)
- Small spots can accommodate compact cars and sedans
- Big spots can accommodate any vehicle type

### Parking Lot
- A collection of parking spots

## Project Structure

```
.
├── README.md
├── src/
│   ├── __init__.py
│   └── models/
│       ├── __init__.py
│       ├── parking_lot.py
│       ├── parking_spot.py
│       └── vehicle.py
└── tests/
    ├── test_parking_lot.py
    ├── test_parking_spot.py
    └── test_vehicle.py
```

## Running Tests

To run tests:

```bash
pytest
```

Or to run specific test files:

```bash
pytest tests/test_vehicle.py
pytest tests/test_parking_spot.py
pytest tests/test_parking_lot.py
```

## Current Implementation

This is a skeleton project with basic class structures and tests. Currently, only the vehicle creation functionality is fully implemented, with the rest of the functionality stubbed for future implementation.