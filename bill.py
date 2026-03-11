units = int(input("Enter the units in bill: "))
bill = (units - 100) * 5
if (units <= 100):
    print("no bill")
elif (units - 100 < 100):
    print(f"You have bill and payable amount is {bill}")
else:
    bill2 = (units - 200) * 10  
    bill3 = bill2 + bill
    print(f"You have bill and payable amount is {bill3}")