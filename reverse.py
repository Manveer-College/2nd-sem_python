num = int(input("Enter the number: "))
org = num
reverse_num = 0
for i in range(len(str(num))):
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num//=10
print(reverse_num) 
if (reverse_num == org):
    print("Pallidrome")
else:
    print("Not Pallidrome")
