color = input("Enter the color: ")
match color:
    case "Black":
        print("Color code: 1 and Multiplier: 1 ohm")   
    case "Red":
        print("Color code: 2 and Multiplier: 10 ohm")
    case "Blue":
        print("Color code: 3 and Multiplier: 100 ohm")
    case _:
        print("Enter right color")
