from collections import defaultdict


# Product Catalog
catalog = {
    'SKU001': {'name': 'Laptop', 'price': 65000, 'category': 'electronics',
               'stock': 15, 'rating': 4.5, 'tags': ['computer', 'work']},

    'SKU002': {'name': 'Smartphone', 'price': 35000, 'category': 'electronics',
               'stock': 10, 'rating': 4.4, 'tags': ['mobile', 'android']},

    'SKU003': {'name': 'Headphones', 'price': 2500, 'category': 'electronics',
               'stock': 0, 'rating': 4.1, 'tags': ['audio', 'music']},

    'SKU004': {'name': 'Smartwatch', 'price': 8000, 'category': 'electronics',
               'stock': 8, 'rating': 4.0, 'tags': ['wearable', 'fitness']},

    'SKU005': {'name': 'Gaming Mouse', 'price': 1500, 'category': 'electronics',
               'stock': 20, 'rating': 4.3, 'tags': ['gaming', 'computer']},

    'SKU006': {'name': 'T-Shirt', 'price': 800, 'category': 'clothing',
               'stock': 30, 'rating': 3.9, 'tags': ['casual', 'cotton']},

    'SKU007': {'name': 'Jeans', 'price': 2000, 'category': 'clothing',
               'stock': 12, 'rating': 4.2, 'tags': ['denim', 'casual']},

    'SKU008': {'name': 'Jacket', 'price': 4500, 'category': 'clothing',
               'stock': 0, 'rating': 4.4, 'tags': ['winter', 'fashion']},

    'SKU009': {'name': 'Sneakers', 'price': 3200, 'category': 'clothing',
               'stock': 25, 'rating': 4.1, 'tags': ['shoes', 'sports']},

    'SKU010': {'name': 'Python Programming', 'price': 900, 'category': 'books',
               'stock': 50, 'rating': 4.6, 'tags': ['programming', 'education']},

    'SKU011': {'name': 'Data Science Handbook', 'price': 1200, 'category': 'books',
               'stock': 18, 'rating': 4.5, 'tags': ['data', 'science']},

    'SKU012': {'name': 'Mystery Novel', 'price': 600, 'category': 'books',
               'stock': 0, 'rating': 3.8, 'tags': ['fiction', 'mystery']},

    'SKU013': {'name': 'Organic Honey', 'price': 450, 'category': 'food',
               'stock': 40, 'rating': 4.7, 'tags': ['organic', 'sweet']},

    'SKU014': {'name': 'Almonds Pack', 'price': 750, 'category': 'food',
               'stock': 22, 'rating': 4.6, 'tags': ['nuts', 'healthy']},

    'SKU015': {'name': 'Dark Chocolate', 'price': 300, 'category': 'food',
               'stock': 0, 'rating': 4.4, 'tags': ['sweet', 'snack']},
}



# Search Products by Tag
def search_by_tag(tag):
    tag_map = defaultdict(list)

    for sku, product in catalog.items():
        for t in product.get('tags', []):
            tag_map[t].append(product)

    return tag_map.get(tag, [])



# Out of Stock Products
def out_of_stock():
    return {
        sku: prod
        for sku, prod in catalog.items()
        if prod.get('stock', 0) == 0
    }



# Filter by Price Range
def price_range(min_price, max_price):
    return {
        sku: prod
        for sku, prod in catalog.items()
        if min_price <= prod.get('price', 0) <= max_price
    }


# Category Summary

def category_summary():
    data = defaultdict(list)

    for product in catalog.values():
        cat = product.get('category')
        if cat:
            data[cat].append(product)

    summary = {}

    for cat, items in data.items():
        count = len(items)
        avg_price = sum(p.get('price', 0) for p in items) / count
        avg_rating = sum(p.get('rating', 0) for p in items) / count

        summary[cat] = {
            "count": count,
            "avg_price": round(avg_price, 2),
            "avg_rating": round(avg_rating, 2)
        }

    return summary



# Apply Discount

def apply_discount(category, percent):
    discount_factor = 1 - percent / 100

    return {
        sku: {**prod, 'price': round(prod.get('price', 0) * discount_factor, 2)}
        if prod.get('category') == category else prod
        for sku, prod in catalog.items()
    }



# Merge Two Catalogs
def merge_catalogs(catalog1, catalog2):
    merged = catalog1 | catalog2  # catalog2 overrides duplicates
    return merged



# Usage
print("Search Tag 'computer':")
print(search_by_tag("computer"))

print("\nOut of Stock:")
print(out_of_stock())

print("\nPrice Range 500 - 5000:")
print(price_range(500, 5000))

print("\nCategory Summary:")
print(category_summary())

print("\nApply 10% Discount on electronics:")
print(apply_discount("electronics", 10))

# Example merge
extra_catalog = {
    "SKU016": {'name': 'Protein Bar', 'price': 120, 'category': 'food',
               'stock': 60, 'rating': 4.3, 'tags': ['healthy', 'snack']}
}

print("\nMerged Catalog Size:")
print(len(merge_catalogs(catalog, extra_catalog)))
