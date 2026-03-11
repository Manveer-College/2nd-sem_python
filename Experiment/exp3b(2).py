num = int(input("Enter the number: "))
print(f"The table for {num} is: ")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")