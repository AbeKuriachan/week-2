# Artifact 7 --- Part D (AI Augmented Task)

## Prompt Used

Design the database schema for a ride‑sharing app like Uber.

Include: - ER diagram - normalized tables - SQL queries using window
functions

## Example Schema

Entities:

Users(UserID, Name, Phone)\
Drivers(DriverID, Name, VehicleID)\
Vehicles(VehicleID, PlateNumber, Type)\
Trips(TripID, RiderID, DriverID, StartTime, EndTime, Fare)\
Payments(PaymentID, TripID, Amount, Method)

## Example SQL Query (Window Function)

Total trips per driver:

SELECT DriverID, COUNT(*) AS total_trips, RANK() OVER (ORDER BY COUNT(*)
DESC) AS driver_rank FROM Trips GROUP BY DriverID;

## Evaluation

Schema is close to 3NF but improvements:

-   Separate driver status history
-   Add location tables
-   Add trip status tracking

Two queries tested successfully on PostgreSQL.
