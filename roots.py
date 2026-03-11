import math as m
a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = float(input("Enter the c: "))
discriminant = b**2 - 4*a*c
if (discriminant > 0):
    root1 = (-b + m.sqrt(discriminant)) / (2 * a)
    root2 = (-b - m.sqrt(discriminant)) / (2 * a)
    print(f'''The roots are {root1:.2f} and {root2:.2f}
    Roots are real and distinct''')
elif (discriminant == 0):
    root = -b / (2 * a)
    print(f'''The root is {root:.2f} and roots are equal
    Roots are real and equal''')
else:
    print("No real roots")  