# Elife Coding Challenge

## Problem Statement : 

We have a lot of rides in New York for tomorrow, and we have a lot of drivers in New York. design a backend algorithm to figure out which ride to give to which driver so that,

* There is no conflict, e.g., we don't give the 2 different rides at 9 AM to the same driver 
* We want to give the ride a lower priced driver if possible. 
* If we give a ride to pick up a passenger from New York time square and drop off the passenger at JFK airport to a driver, the next ride we give to the same driver should preferably pick up from JFK airport, this way, the driver doesn't have to drive a lot without a paying passenger on the car. 
* You may assume as input a collection of rides. Each ride consists of pickup time, pickup location (latitude/longitude), pickup address, drop off location/address and estimated ride duration.

## Assumptions : 

* Driver Availability: Each driver has a schedule which lists their booked rides with start and end times. If a new ride overlaps with any of these times, the driver is not available for that ride.
* Distance Calculation: The distance between two locations is calculated using Euclidean distance for simplicity, although in a real-world scenario, a more accurate measure can be used.
* Ride Times: The pickup time of each ride is given and the ride duration is in minutes. The ride ends exactly after the given duration.
* Drivers Sorted by Price: Drivers are sorted by price, and the algorithm tries to assign a ride to the lowest-priced available driver.
* No Driver Available: If no driver is available at the given time, the ride pickup time is incremented by 1 minute until a driver becomes available.

## Corner Cases : 

* No Available Drivers: If no drivers are available for the initial ride time, the algorithm will continuously increment the ride's pickup time until a driver becomes available.
* Multiple Rides at the Same Time: The algorithm handles multiple rides with the same pickup time by assigning the best available driver to each ride sequentially.
* Driver's Location Update: After each ride, the driver's current location is updated to the drop-off location of the last assigned ride.
* High-Density Pickup Locations: Multiple rides from the same pickup location to different drop-off locations can result in drivers moving out of the pickup area. The algorithm prioritizes assigning rides to drivers already near the pickup location.
* Edge Case for Empty Schedule: If a driver has no rides assigned yet, their availability is only checked based on their current location.

## Solution :

* Sorting Drivers: Drivers are sorted by their pricing to prioritize lower-cost drivers.
* Ride Assignment: Each ride is assigned to the best available driver. The best driver is determined based on availability and proximity to the pickup location.
* Conflict Checking: A function is_available checks for scheduling conflicts by ensuring no overlapping times.
* Location Update: After assigning a ride, the driver's current location is updated to the ride's drop-off location.
* Pickup Time Adjustment: If no driver is available at the initial pickup time, the time is incremented by 1 minute until a driver becomes available.

## Time-Complexity : 

* Sorting Drivers by Price: D(log D) where D is number of drivers
* Checking Availability for Each Ride: In the worst case, each ride may need to check every driver. For each driver, checking the schedule involves iterating over their rides, assuming each driver has R rides, the complexity for this O(R*D)
* Distance Calculation: Each distance calculation is O(1) but since it's done for every ride-driver pair, the complexity is O(R*D)
* Overall time complexity : O(Dlog D + R*D) 

## Optimizations that can be done : 

* Priority queue to maintain drivers sorted by distance to the pickup location for efficient retrieval of the closest available driver.
* KD Trees for spatial queries and can significantly reduce the time to find nearby drivers.