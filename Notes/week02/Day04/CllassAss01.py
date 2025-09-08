import BillCalciBase as bc

without = bc.calculate_bill(quantity=4, item_cost=500)
print(f"Bill 10:{without}")

withi = bc.calculate_bill(500, 4, 5, 10)
print(f"Bill 11: {withi}")

# Only positional
print("Bill 1:", bc.calculate_bill(500, 2))

# With custom tax
print("Bill 2:", bc.calculate_bill(500, 2, tax=0.1))

# With custom discount
print("Bill 3:", bc.calculate_bill(500, 2, discount=50))
# With custom tax and discount
print("Bill 4:", bc.calculate_bill(500, 2, tax=0.08, discount=100))

