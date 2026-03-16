# Artifact 7 --- Part C (Interview Ready)

## Q1 --- Update Anomalies

Denormalised databases create three anomalies.

### Update anomaly

Same information stored multiple times.

Example:

  OrderID   Product   Price
  --------- --------- -------
  101       Laptop    50000
  102       Laptop    50000

If price changes to 52000 and only one row updated, data becomes
inconsistent.

### Insertion anomaly

Cannot insert product without creating an order row.

### Deletion anomaly

Deleting the last order of a product removes product information.

Normalization solves these problems.

------------------------------------------------------------------------

## Q2 --- Schema for Current Price and Price History

Products

| ProductID \| ProductName \| CurrentPrice \|

PriceHistory

| HistoryID \| ProductID \| Price \| StartDate \| EndDate \|

Relationships:

PriceHistory.ProductID → Products.ProductID

This schema satisfies 3NF because non‑key attributes depend only on the
primary key.

------------------------------------------------------------------------

## Q3 --- Hotel Room Double Booking

ACID property at risk: **Isolation**

Scenario:

Two users read that one room is available and both attempt booking.

Without isolation both transactions commit causing double booking.

Databases prevent this using:

-   row level locks
-   serializable isolation level
-   transactions

Example:

BEGIN TRANSACTION\
Check room availability\
Reserve room\
COMMIT

If conflict occurs → ROLLBACK.
