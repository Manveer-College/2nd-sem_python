value = int(input("Enter the frequency: "))
if 3 * 100 <= value * 1000 <= 30 * 1000:
    print(f"{value}KHz is VLF")
elif 30 * 1000 <= value * 1000 <= 300 * 1000:
    print(f"{value}KHz is LF")
elif 300 * 1000 <= value * 1000 <= 3 * 1000 * 1000:
    print(f"{value}KHz is MF")

# not