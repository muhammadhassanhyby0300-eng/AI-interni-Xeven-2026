username = input("Enter your name:")
Password = input("Enter your password:")
Age = int(input("Enter your age:"))
if len(username)<5:
    print("Username must be at least 5 characters long.")
elif len(Password)<8:
    print("Password must be at least 8 characters long.")
elif Age<18:
    print("You must be at least 18 years old to register.")
else:
    print("Registration successful!")
    #In this program I take input from user and confirms 
    # it using if else statements. 