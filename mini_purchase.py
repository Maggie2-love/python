
add_product = "yes"
name = input("Enter your name: ")
total_amount = 0
while add_product == "yes":

    product_name = input("Enter the product you got: ")

    quantity = int(input("Enter the quantity of  product: " ))

    price = float(input("Enter the price of product: " ))

    add_product = input("Add another product. yes/no: ")
    
    amount = quantity * price
    total_amount+= amount
    

print("Your total amount is:" , total_amount)
