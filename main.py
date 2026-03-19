#TASK 1 - A

# a)
customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

# b)

subtotal = price * quantity

if subtotal>5000:
    print("Subtotal: ", subtotal)
    discount = subtotal * 0.1
    total = subtotal - discount
    print("Discount: ", discount)
    print("Total: ", total)
else:
    print("Total: ", subtotal)





