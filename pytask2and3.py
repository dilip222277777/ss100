#email validation
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))
email = input("Enter email: ").strip()  
if is_valid_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is NOT a valid email address.")

#user logiin with password and username
import hashlib
import getpass  


users_db = {}

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Register a new user with username and password"""
    print("\n--- User Registration ---")
    username = input("Enter username: ").strip()
    
    if username in users_db:
        print("Username already exists!")
        return
    
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords don't match!")
        return
    
    hashed_password = hash_password(password)
    users_db[username] = hashed_password
    print("Registration successful!")

def login_user():
    """Authenticate a user"""
    print("\n--- User Login ---")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    
    if username not in users_db:
        print("Invalid username or password!")
        return False
    
    hashed_password = hash_password(password)
    if users_db[username] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password!")
        return False

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select option (1-3): ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


