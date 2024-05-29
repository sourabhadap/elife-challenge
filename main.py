import math
from datetime import datetime, timedelta
from typing import List


class Ride:
    def __init__(self, pickup_time: datetime, pickup_location: tuple, dropoff_location: tuple, duration: int):
        self.pickup_time = pickup_time
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.duration = duration


class Driver:
    def __init__(self, driver_id, price, current_location):
        self.driver_id = driver_id
        self.price = price
        self.current_location = current_location
        self.schedule = []  # List of (start_time, end_time, dropoff_location)


def is_available(driver: Driver, ride: Ride):
    for (start_time, end_time, _) in driver.schedule:
        if not (ride.pickup_time >= end_time or (ride.pickup_time + timedelta(minutes=ride.duration)) <= start_time):
            return False
    return True


def calculate_distance(loc1, loc2):
    return math.dist([loc2[0] - loc1[0]], [loc2[1] - loc1[1]])


def assign_rides_to_drivers(rides: List[Ride], drivers: List[Driver]):
    # sort drivers by price
    drivers.sort(key=lambda d: d.price)

    assignments = {}

    for ride in rides:
        best_driver = None
        best_distance = float('inf')

        while ride not in assignments:
            # find the best driver
            for driver in drivers:
                if is_available(driver, ride):
                    distance_to_pickup = calculate_distance(driver.current_location, ride.pickup_location)
                    print(f"Distance to {driver.driver_id} : {distance_to_pickup}")
                    if distance_to_pickup < best_distance:
                        best_distance = distance_to_pickup
                        best_driver = driver

            if best_driver:
                # assign the ride to the best driver
                assignments[ride] = best_driver.driver_id
                # update drivers schedule
                ride_end_time = ride.pickup_time + timedelta(minutes=ride.duration)
                best_driver.schedule.append((ride.pickup_time, ride_end_time, ride.dropoff_location))
                # update drivers current location
                best_driver.current_location = ride.dropoff_location
            else:
                # no driver available
                print("Driver not available")
                ride.pickup_time += + timedelta(minutes=1)
    return assignments


# Input
rides = [
    Ride(datetime(2024, 5, 28, 9, 0), (40.758896, -73.985130), (40.6413111, -73.7781391), 25),
    Ride(datetime(2024, 5, 28, 9, 0), (40.758896, -73.985130), (60.6413111, -79.7781391), 30),
    Ride(datetime(2024, 5, 28, 9, 0), (40.758896, -73.985130), (50.6413111, -69.7781391), 50),
    # Ride(datetime(2024, 5, 28, 10, 0), (40.6413111, -73.7781391), (40.758896, -73.985130), 30),
    # Ride(datetime(2024, 5, 28, 11, 0), (45.6413111, -79.7781391), (50.758896, -98.985130), 25),
    # Ride(datetime(2024, 5, 28, 12, 0), (65.6413111, -89.7781391), (100.758896, -118.985130), 60),
]

drivers = [
    Driver("driver_1", 10, (40.758896, -73.985130)),
    Driver("driver_2", 12, (40.6413111, -73.7781391)),
]

assignments = assign_rides_to_drivers(rides, drivers)
for ride, assignment in assignments.items():
    print(f"Ride at {ride.pickup_time} is assigned to driver {assignment}")
