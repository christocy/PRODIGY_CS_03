import re

# Function to check the complexity of the password
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*#?&]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, $, !, etc.).")

    return strength, feedback

# Function to provide feedback on password strength
def evaluate_password(password):
    strength, feedback = check_password_strength(password)

    if strength == 5:
        return "Password is very strong!"
    elif strength == 4:
        return "Password is strong."
    elif strength == 3:
        return "Password is moderate."
    elif strength == 2:
        return "Password is weak."
    else:
        return "Password is very weak.", feedback

# Input from the user
password = input("Enter your password: ")

# Call the function to evaluate the password
strength_feedback = evaluate_password(password)

# Output the result
if isinstance(strength_feedback, tuple):
    print(strength_feedback[0])
    print("Feedback:")
    for fb in strength_feedback[1]:
        print("- " + fb)
else:
    print(strength_feedback)
