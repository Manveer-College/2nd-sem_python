line = input("Enter the line to be added in the file: ")
with open("exp10(b).txt", "a") as file:
    file.write(line + "\n")
    file.close()
with open("exp10(b).txt", "r") as file:
    data = file.read()
    print(data)
    print("Here is cursor:", file.tell())
    file.seek(0) #this reset cursor to 0
    data1 = file.read()
    print(data1)