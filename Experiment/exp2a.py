print("This only tells the frequncy is wheter Audio or Radio")
a = int(input("Enter the frequency: "))
c = 3e11
if (20 <= a <= 20000 ):
    print(f"{a}Hz is Audio")
elif (30000 <= a <= c):
    print(f"{a}Hz is Radio")
else:
    print("You Enter wrong Frequency")