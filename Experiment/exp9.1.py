def area(l=5, b=10):
    return l * b
    
#calling default
print(area())

#calling with one arguments, 2nd is default
print(area(10))

#calling with two arguments
print(area(10, 20))

#calling with 1nd arguments as default
print(area(b=20))