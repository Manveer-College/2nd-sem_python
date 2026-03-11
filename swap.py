a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
print(f"These are numbers you enter {a}, {b}")

temp = a
a = b
b = temp

print(f"These are numbers swapped {a}, {b}")