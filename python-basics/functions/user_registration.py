def get_input():
    return {
        "username": "vimal_anand",
        "email": "vimal@example.com",
        "age": 22
    }
# using a function to get user input data, static for this example.


def validate_input(user_data):
    if not user_data["username"]:
        return False
    if "@" not in user_data["email"]:
        return False
    if user_data["age"] < 18:
        return False
    return True
# Validates user input data.


def save_to_db(user_data):
    print("Saving user to database...")
    print(f"User saved: {user_data['username']} ({user_data['email']})")
# Simulates saving user data to a database.


def register_user():
    user_data = get_input()
    if not validate_input(user_data):
        print("Invalid user data. Registration failed.")
        return
    save_to_db(user_data)
    print("User registered successfully!")
# Main function to handle user registration.



register_user()
# Trigger the user registration process.
