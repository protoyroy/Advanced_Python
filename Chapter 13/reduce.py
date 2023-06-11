from functools import reduce

cart = [
    {"item": "T-Shirt", "price": "19.99"},
    {"item": "Jeans", "price": "49.99"},
    {"item": "Shoes", "price": "79.99"},
    {"item": "Hat", "priCe": "9.99"},
    {"item": "Shorts", "Price": "1" }
]

total_price = reduce(lambda acc, item: acc + float(item.get("price", "0").strip()), cart, 0)
print("Total Price (Before Fix):", total_price)

# Convert keys to lowercase
cart = [{k.lower(): v for k, v in item.items()} for item in cart]

total_price = reduce(lambda acc, item: acc + float(item.get("price", "0").strip()), cart, 0)
print("Total Price (After Fix):", total_price)