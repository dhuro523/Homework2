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

def calculate_total(orders):
    grand_total = 0
    print("Order Summary: ")
    print("----------------------")
    for order in orders:
        order_total = order["price"] * order["quantity"]
        grand_total += order_total
        print(f"Order ID: {order['order_id']}, Price: {order['price']}, Quantity: {order['quantity']}, Total: {order_total}")
        
    print("----------------------")
    print(f"Grand Total: {grand_total}")

valid_orders = validate_orders(orders)
calculate_total(valid_orders)