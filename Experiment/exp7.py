student = {
    "Roll number" : 2555700,
    "name" : "Manveer Singh",
    "age" : 19
}

print(student)

#accessing by only key value pairs
print(student.get("name"))
print(student["age"])

print(list(student.items()))
print(list(student.keys()))
print(list(student.values()))

#add and update
student["Pincode"] = 147001
student.update({"city" : "Patiala"})
print(student)

#delete items
student.pop("Pincode")
student.popitem()
del student["Roll number"]
print(student)

a = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

#min and max, assending and decending
print(max(a.values()))
print(min(a.values()))
print(sorted(a.items()))
print(sorted(a.items(), reverse=True))
print(sorted(a.keys()))
print(sorted(a.keys(), reverse=True))
print(sorted(a.values()))
print(sorted(a.values(), reverse=True))
