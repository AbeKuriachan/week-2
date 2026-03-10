from collections import namedtuple
import timeit

# ---------------------------------------------------------
#  Frozenset
# ---------------------------------------------------------

"""
What is frozenset?

A frozenset is an immutable version of a Python set. Once created,
its elements cannot be modified (no add, remove, or update operations).

Example:
s = frozenset({1,2,3})

Difference between set and frozenset

set
- Mutable
- Elements can be added or removed
- Cannot be used as dictionary keys
- Syntax: {1,2,3}

frozenset
- Immutable
- Cannot be changed after creation
- Can be used as dictionary keys
- Syntax: frozenset({1,2,3})

When to use it in real systems

frozenset is useful when:
- You need an immutable collection
- The set must be used as a dictionary key
- You want to guarantee the data will not change

Examples in real systems:
- Bundle discount rules
- Permission sets
- Configuration groups
"""

# ---------------------------------------------------------
# Product structure
# ---------------------------------------------------------

Product = namedtuple("Product", ["id", "name", "category", "price"])

catalog = [
    Product(1,"Laptop","Electronics",75000),
    Product(2,"Phone","Electronics",50000),
    Product(3,"Headphones","Electronics",3000),
    Product(4,"Smartwatch","Electronics",8000),

    Product(5,"Tshirt","Clothing",1000),
    Product(6,"Jeans","Clothing",2000),
    Product(7,"Jacket","Clothing",3500),

    Product(8,"Clean Code","Books",600),
    Product(9,"Python Crash Course","Books",700),
    Product(10,"Atomic Habits","Books",500),

    Product(11,"Lamp","Home",1200),
    Product(12,"Chair","Home",2500),
    Product(13,"Coffee Maker","Home",4500),
    Product(14,"Desk","Home",6000),
    Product(15,"Shelf","Home",3000)
]

# ---------------------------------------------------------
#  Bundle Discount System
# ---------------------------------------------------------

bundle_discounts = {
    frozenset({"Electronics","Books"}): 10,
    frozenset({"Clothing","Home"}): 15,
    frozenset({"Electronics","Home"}): 12
}

# ---------------------------------------------------------
#  Bundle Checker Function
# ---------------------------------------------------------

def check_bundle_discount(cart):

    # Get categories in the cart
    cart_categories = {product.category for product in cart}

    applicable_discounts = [
        discount
        for bundle, discount in bundle_discounts.items()
        if bundle.issubset(cart_categories)
    ]

    return max(applicable_discounts, default=0)


#cart
cart = {catalog[0], catalog[8], catalog[10]}
# Laptop (Electronics) + Python Crash Course (Books) + Lamp (Home)

discount = check_bundle_discount(cart)

print("Discount applied:", discount, "%")

# ---------------------------------------------------------
# Performance Benchmark
# ---------------------------------------------------------

set_time = timeit.timeit("set([1,2,3,4])", number=100000)
frozenset_time = timeit.timeit("frozenset([1,2,3,4])", number=100000)

print("\nPerformance Benchmark")
print("Set creation time:", set_time)
print("Frozenset creation time:", frozenset_time)

"""
Results:

Set creation time:       ~0.052 seconds
Frozenset creation time: ~0.030 seconds

Conclusion:
- frozenset creation is slightly faster
- performance difference is usually negligible
"""