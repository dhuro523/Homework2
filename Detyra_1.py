orders = [{"order_id": 1, "price": 50, "quantity": 2},
          {"order_id": 2, "price": -10, "quantity": 1},
          {"order_id": 3, "price": 30, "quantity": 0},
          {"order_id": 4, "price": 20, "quantity": 3},
]

def validate_orders(orders):
    valid_orders = []
    for order in orders:
        if order["price"] > 0 and order["quantity"] > 0:
            valid_orders.append(order)
    return valid_orders

result = validate_orders(orders)
print(result)