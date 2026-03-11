print("Enter the numbers")
maths = int(input("Enter your Maths marks: "))
chem = int(input("Enter your Chem marks: "))
python = int(input("Enter your Python marks: "))
eng = int(input("Enter your English marks: "))
total = int(input("Enter the total number: "))

marks = (maths + chem + python + eng)/total * 100

if (marks >= 40):
    print(f"You having {marks}%, You Passed!")
else:
    print(f"You having {marks}%, You Failed Noob!")