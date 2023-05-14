import re


def is_valid_email(email: str) -> bool:
    """Validate email address format"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    """Validate phone number format (Egyptian phone numbers only)"""
    pattern = r'^01[0-9]{9}$'
    return bool(re.match(pattern, phone))


def register() -> None:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    while True:
        email = input("Enter your email address: ")
        if is_valid_email(email):
            break
        print("Invalid email address. Please enter a valid email address.")

    password = input("Enter your password: ")

    while True:
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        print("Passwords do not match. Please confirm your password again.")

    while True:
        phone = input("Enter your mobile phone number: ")
        if is_valid_phone(phone):
            break
        print("Invalid phone number. Please enter a valid Egyptian phone number.")

    with open("usersDB.txt", "a") as file:
        file.write(f"{first_name} {last_name} {email} {password} {phone}\n")

    print("Registration successful.")


def login() -> None:
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    with open("usersDB.txt", "r") as file:
        for line in file:
            user_info = line.strip().split()
            if user_info[2] == email and user_info[3] == password:
                print("Login successful.")
                print(f"Welcome, {user_info[0]} {user_info[1]}!")
                return
    print("Invalid email or password. Please try again.")
    login()
