a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

print("---------arithmetic operators---------")
print(f"Additiono of {a} and {b} is {a + b}")
print(f"Substatiom of {a} and {b} is {a - b}")
print(f"Multiplication of {a} and {b} is {a * b}")
print(f"Division of {a} and {b} is {a / b}")
print(f"Modulus of {a} and {b} is {a % b}")
print(f"Exponentiation of {a} and {b} is {a ** b}")
print(f"Floor division of {a} and {b} is {a // b}")

print("---------comparison operators---------")
print(f"Equal to of {a} and {b} is {a == b}")
print(f"Not equal to of {a} and {b} is {a != b}")
print(f"Greater than of {a} and {b} is {a > b}")
print(f"Less than of {a} and {b} is {a < b}")
print(f"Greater than or equal to of {a} and {b} is {a >= b}")
print(f"Less than or equal to of {a} and {b} is {a <= b}")

print("---------logical operators---------")
print(f"And of {a} and {b} is {a and b}")
print(f"Or of {a} and {b} is {a or b}")
print(f"Not of {a} is {not a}")

print("---------assignment operators---------")
a = b
print(f"Value of {a}")
a += b
print(f"Value of {a}")
a -= b
print(f"Value of {a}")
a *= b
print(f"Value of {a}")
a /= b
print(f"Value of {a}")
a **= b
print(f"Value of {a}")
a //= b
print(f"Value of {a}")
a %= b
print(f"Value of {a}")

print("---------bitwise operators---------")
a = int(input("Enter the 1st number for bitwise: "))
b = int(input("Enter the 2nd number for bitwise: "))
print(f"Bitwise AND of {a} and {b} is {a & b}")
print(f"Bitwise OR of {a} and {b} is {a | b}")
print(f"Bitwise XOR of {a} and {b} is {a ^ b}")
print(f"Bitwise NOT of {a} is {~a}")
print(f"Bitwise LEFT SHIFT of {a} by {b} is {a << b}")
print(f"Bitwise RIGHT SHIFT of {a} by {b} is {a >> b}")

print("---------membership operators---------")
a = input("Enter the string: ")
b = input("Enter the character to be find out in string: ")
print(f"Is {b} in the string {a}? {b in a}")
print(f"Is {b} not in the string {a}? {b not in a}")

print("---------identity operators---------")
a = int(input("Enter the 1st number for identity: "))
b = int(input("Enter the 2nd number for identity: "))
print(f"Is {a} is the same as {b}? {a is b}")
print(f"Is {a} is not the same as {b}? {a is not b}")