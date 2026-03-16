# Artifact 7 --- Part A (ER Modelling, Normalisation, Relational Algebra)

## 1. ER Diagram --- Online Food Delivery App

Entities: - Customer(CustomerID, Name, Email, Phone) -
Restaurant(RestaurantID, Name, Location) - MenuItem(ItemID,
RestaurantID, ItemName, Price) - Order(OrderID, CustomerID,
RestaurantID, OrderTime, Status) - OrderItem(OrderItemID, OrderID,
ItemID, Quantity) - DeliveryPartner(PartnerID, Name, Phone) -
Delivery(DeliveryID, OrderID, PartnerID, DeliveryTime, Status)

Cardinality:

Customer (1) ------ (M) Order\
Restaurant (1) ------ (M) MenuItem\
Restaurant (1) ------ (M) Order\
Order (1) ------ (M) OrderItem\
MenuItem (1) ------ (M) OrderItem\
DeliveryPartner (1) ------ (M) Delivery\
Order (1) ------ (1) Delivery


## 2. Normalisation of Flat Table (OrderFacts) csv not provided

Flat Table ():

  OrderID   CustomerName   Product   Price   Quantity
  --------- -------------- --------- ------- ----------

### Step 1 --- 1NF

Ensure atomic columns.

| OrderID \| CustomerName \| Product \| Price \| Quantity \|

### Step 2 --- 2NF

Remove partial dependency.

Tables:

Customers(CustomerID, CustomerName)\
Orders(OrderID, CustomerID)\
Products(ProductID, ProductName, Price)\
OrderItems(OrderID, ProductID, Quantity)

### Step 3 --- 3NF

Remove transitive dependency.

Final Schema:

Customers(CustomerID, Name)\
Products(ProductID, Name, Price)\
Orders(OrderID, CustomerID)\
OrderItems(OrderID, ProductID, Quantity)

## 3. Relational Algebra Queries

1.  All orders placed by a specific customer

σ CustomerID = 101 (Orders)

2.  Names of all customers

π Name (Customers)

3.  Orders with customer details

Orders ⋈ Customers

4.  All product names ordered

π ProductName (Products ⋈ OrderItems)

5.  Customers who placed orders

π CustomerID (Orders)

## 4. Pandas → Relational Algebra Mapping

  Pandas Operation     Relational Algebra
  -------------------- ----------------------
  df\[df.col \> 10\]   Selection (σ)
  df\[\['name'\]\]     Projection (π)
  pd.merge(A,B)        Join (⋈)
  groupby().agg()      Grouping/Aggregation
