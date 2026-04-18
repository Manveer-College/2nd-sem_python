class UnderAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is too young to vote")

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise UnderAgeError(age)
    print("You are eligible to vote")
except UnderAgeError as e:
    print(e)
except TypeError:
    print("Enter only integer value")
finally:
    print("Thank you for using our program")