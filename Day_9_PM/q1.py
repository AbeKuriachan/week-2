from collections import namedtuple

#  Define Named Tuple
Product = namedtuple("Product", ["id", "name", "category", "price"])


# Create Product Catalog (15 products, 4 categories)

catalog = [
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Smartphone", "Electronics", 50000),
    Product(3, "Headphones", "Electronics", 3000),
    Product(4, "Smartwatch", "Electronics", 8000),

    Product(5, "T-Shirt", "Clothing", 1000),
    Product(6, "Jeans", "Clothing", 2000),
    Product(7, "Jacket", "Clothing", 3500),
    Product(8, "Sneakers", "Clothing", 4000),

    Product(9, "Clean Code", "Books", 600),
    Product(10, "Python Crash Course", "Books", 700),
    Product(11, "Atomic Habits", "Books", 500),
    Product(12, "Deep Work", "Books", 550),

    Product(13, "Lamp", "Home", 1200),
    Product(14, "Chair", "Home", 2500),
    Product(15, "Coffee Maker", "Home", 4500),
]

# Assign variables
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 = catalog


# Customer Cart Sets

customer_1_cart = {p1, p5, p9, p13}
customer_2_cart = {p2, p6, p9, p14}
customer_3_cart = {p3, p7, p10, p15}
customer_4_cart = {p3, p5, p11, p13}
customer_5_cart = {p3, p8, p9, p12}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
]


# Analyze Shopping Behaviour

# (a) Bestsellers (products in ALL carts)
bestsellers = set.intersection(*all_carts)

# (b) Catalog Reach (products in ANY cart)
catalog_reach = set.union(*all_carts)

# (c) Exclusive Purchases (only customer 1 bought)
others = set.union(customer_2_cart, customer_3_cart, customer_4_cart, customer_5_cart)
exclusive_customer1 = customer_1_cart - others


# Product Recommendation

def recommend_products(customer_cart, all_carts):
    all_products = set.union(*all_carts)
    return all_products - customer_cart


# Category Summary

def category_summary():
    categories = {p.category for p in catalog}

    summary = {
        category: {p.name for p in catalog if p.category == category}
        for category in categories
    }

    return summary


print("Bestsellers (in all carts):")
print({p.name for p in bestsellers})

print("\nCatalog Reach (any cart):")
print({p.name for p in catalog_reach})

print("\nExclusive purchases of Customer 1:")
print({p.name for p in exclusive_customer1})

print("\nRecommended for Customer 1:")
print({p.name for p in recommend_products(customer_1_cart, all_carts)})

print("\nCategory Summary:")
print(category_summary())