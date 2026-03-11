name = input("Enter your name: ")
for j in range(0, len(name) + 1):
    for i in range(0,j):
        print(name[i], end = "")
    print()