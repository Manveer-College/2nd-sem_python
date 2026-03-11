student = ("Manveer Singh", 19, "Patiala", "CSE", 90, 80, 70, 60, 50)
print(student)

#access the tuple
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])
print(student[5])
print(student[6])
print(student[7])
print(student[8])
print(student[0:4])

#concatenate and repeatation the tuple
extrainfo = ("Day Scholar", "Male", "23-02-2007")
student += extrainfo
print(student)
print((student[2],) * 2)

#membership
print("Manveer" in student)
print("Manveer" not in student)

#iteration the tuple
for i in student:
    print(i)

#updation via list
student = list(student)
student[0] = "Manveer"
student = tuple(student)
print(student)

# tupple t containg the studen name and marks to create seprate 2 list one contain name and other for score .................................