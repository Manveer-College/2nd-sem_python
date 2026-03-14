#write a program to create a function show_employ write the following specs name and salary , it should display both, if salary not ptovide in call it would default to 9000
class show_employ():
    def show_name(self, name):
        return name

    def show_salary(self, salary = 9000):
        return salary

name = input("Enter the name: ")
salary = input("Enter the salary: ")

emp = show_employ()

print("The name of the Employ is: ", emp.show_name(name))
if salary =="":
    print(f"The salary of {emp.show_name(name)} is {emp.show_salary()}")
else:
    
    print(f"The salary of {emp.show_name(name)} is {emp.show_salary(salary)}")