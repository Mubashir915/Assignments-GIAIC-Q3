import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least 8 characters long.")

    # Rule 2: Uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one uppercase letter (A-Z).")

    # Rule 3: Lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one lowercase letter (a-z).")

    # Rule 4: Digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("⚠️ Add at least one number (0-9).")

    # Rule 5: Special characters
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("⚠️ Include at least one special character (!@#$%^&*).")

    # Score interpretation
    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Moderate ⚠️"
    else:
        strength = "Strong ✅"

    return score, strength, feedback


# Main program
if __name__ == "__main__":
    print("🔐 Password Strength Meter")
    user_password = input("Enter your password: ")
    score, strength, suggestions = check_password_strength(user_password)

    print(f"\n🔎 Password Strength: {strength} (Score: {score}/5)")

    if strength != "Strong ✅":
        print("\n💡 Suggestions to improve your password:")
        for item in suggestions:
            print(f" - {item}")
    else:
        print("✅ Great! Your password is strong and secure.")
