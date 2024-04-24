def check_password(password):
    min_length = 8
    if len(password) < min_length:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    if not any(char in special_chars for char in password):
        return False
    return True

password = input("Enter a password: ")
if check_password(password):
    print("The password is valid.")
else:
    print("The password is not valid. Please make sure it is at least 8 characters long, contains at least one digit, one lowercase letter, one uppercase letter, and one special character.")