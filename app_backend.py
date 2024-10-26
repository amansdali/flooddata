

user_data = {
    "username": "user123",
    "password": "securepassword"
}


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == user_data["username"] and password == user_data["password"]:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

if len(user_data) == 0: 
    global additional_data
    username = input("What is your email?: ")
    pwd = input("Type a secure password: ")
else: 
    login()
