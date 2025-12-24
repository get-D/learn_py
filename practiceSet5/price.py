# Given a dictionary of products and their prices, find the product with the highest price.

prodCost = {"chocolate": 110, "teady": 250, "earphones": 199, "coke": 20}

prod = max(prodCost, key = prodCost.get)

print(f"{prod} has the highest price")