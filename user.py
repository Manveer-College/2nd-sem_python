choice = int(input('''Enter the choice: 
1. Create a new user
2. Login to the system
'''))
users = {
    "manveer": "1234",
    "rahul": "5678",
}
if choice == 1:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    users.update({username: password})
    print("User created successfully")
    print("Login to the system")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Login failed")
elif choice == 2:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Invalid choice")