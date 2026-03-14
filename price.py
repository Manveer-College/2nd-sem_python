#calculate theh prioce of an item if quantity is given take default value of tax 5% and discount price 0 if number of quantity is greater than 10 then discount 10% on price

def bill(price, quantity, tax=5, discount=10):
    price = quantity * 100
    if quantity < 10:
        return price + (price * tax / 100)
    else:
        return price + (price * tax / 100) - (price * discount / 100)


price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

print("The total bil: ", bill(price, quantity))