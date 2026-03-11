name = input("Enter your name: ")
# square
rows = 5
for i in range(1, rows + 1):
    print("* " * (rows))
print()

# rectangle
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
print()

#inverted
rows = 5
for i in range(1, rows + 1):
    print("* " * rows)
    rows -= 1
print()

#pyramid
rows = 5
for i in range(1, rows +1):
    print(" " * (rows - i) + "* " * i)
print()

#pattern
for j in range(0, len(name) + 1):
    for i in range(0,j):
        print(name[i], end = "")
    print()