from functools import reduce


sum = lambda a, b: a+b 

l = [1, 2, 3, 4,]
value = reduce (sum, l)
print(value)   #reduce work as sequantial computation

# Example: Calculating the total price of items in a shopping cart



cart = [
    {"item": "T-Shirt", "price": 19.99},
    {"item": "Jeans", "Price": 49.99},
    {"item": "Shoes", "PRICE": 79.99},
    {"item": "Hat", "Price": 9.99},
    {"item": "Bike", "pRice": 1}
]

# Convert keys to lowercase
cart = [{a.lower(): b for a, b in item.items()} for item in cart]

total_price = reduce(lambda acc, item: acc + float(str(item.get("price", 0)).strip()), cart, 0)
print("Total Price:", total_price)


# total_price = lambda x , y : x + y["price"]         #to understand the code properly snippet
# value2 = reduce (total_price, cart,0)


 #prints "Total Price: 159.96"
 #print(value2)