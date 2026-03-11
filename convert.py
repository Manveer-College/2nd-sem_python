c = int(input('''Enter what you want to convert
              Enter 1 for KM into Miles
              Enter 2 for Miles into KM '''))
if (c == 1):
    a = float(input("Enter the KM: "))
    conv = 0.621371
    d = a * conv
    print(f"Here is the mile {d}")
elif (c == 2):
    a = float(input("Enter the miles: "))
    conv = 0.621371
    d = a / conv
    print(f"Here is the mile {d}")

