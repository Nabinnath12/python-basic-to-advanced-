full_name = input("Please enter your full name: ")

email = input("Please enter your email: ")
phone = input("Please enter your phone number: ")
address = input("Please enter your address: ")

while True:
    password = input("Please enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password == confirm_password:
        print("Registration successful ✅")
        break
    else:
        print("❌ Passwords do not match, please try again.")

# Store user data in a dictionary
user_data = {
    "full_name": full_name,
    "email": email,
    "phone": phone,
    "address": address,
    "password": password
}

print("\nWelcome to our login page:")
login_email = input("Enter your email: ")
login_password = input("Enter your password: ")

if login_email == user_data["email"] and login_password == user_data["password"]:
    print("Login successful ✅")
    print(f"Welcome {user_data['full_name']} 🎉")
else:
    print("❌ Invalid username or password. ! ❤️ ") 
