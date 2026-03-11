list = ["Manveer", "Rahul", "Raj", "Rohit", "Rajesh"]
print(f"The list of names is: {list}")

# Access the list
print(f"The first name in list is: {list[0]}")
print(f"The last name in list is: {list[-1]}")
print(f"List from 1 to 3: {list[1:3]}")

#Update the list
list[2] = "Karan"
print(f"The list after updating the name is: {list}")

#Add a new name to the list
list.insert(1, "Jaspreet")
list.append("Sharan")
print(f"The list after adding the name is: {list}")

#Remove a name from the list
list.remove("Karan")
print(f"The list after removing the name is: {list}")

del list[1]
print(f"The list after deleting the name is: {list}")

list.pop()
print(f"The list after popping the name is: {list}")

list.clear()
print(f"The list after clearing the name is: {list}")