t = ("Manveer Singh", 93, "Priya", 72, "Rajesh", 65, "Raj", 58, "Rohit", 49)
name = []
marks = []
for item in t:
    if type(item) == int:
        marks.append(item)
    elif type(item) == str:
        name.append(item)
print(name)
print(marks)