def add(a=10, b=20):
    return a + b

#calling default
print(add())

#calling with one arguments, 2nd is default
print(add(20))

#calling with two arguments
print(add(20, 30))

#calling with 1nd arguments as default
print(add(b=30))