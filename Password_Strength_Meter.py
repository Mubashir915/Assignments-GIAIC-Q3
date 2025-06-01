import streamlit as st
import re
import random
import string

# Function to evaluate password strength
def evaluate_password(password):
    issues = []
    strength_score = 0

    # Check if password is long enough
    if len(password) >= 8:
        strength_score += 1
    else:
        issues.append("❌ Password should be at least 8 characters long.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength_score += 1
    else:
        issues.append("❌ Include both uppercase and lowercase letters.")

    # Check for at least one digit
    if re.search(r"\d", password):
        strength_score += 1
    else:
        issues.append("❌ Add at least one number (0-9).")

    # Check for at least one special character
    if re.search(r"[!@#$%^&*\-_+=]", password):
        strength_score += 1
    else:
        issues.append("❌ Include at least one special character (!@#$%^&*-_+=).")

    # Determine the strength rating
    if strength_score == 4:
        issues.append("✅ Strong Password!")
    elif strength_score == 3:
        issues.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        issues.append("❌ Weak Password - Improve it using the suggestions above.")

    return issues, strength_score

# Function to create a random strong password
def create_strong_password():
    length = 12
    # Combine letters, numbers, and special characters
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=]"
    # Randomly select characters to form the password
    password = "".join(random.choice(chars) for _ in range(length))
    return password

# Main function to run the Streamlit app
def main():
    st.title("🔐 Password Strength Checker")
    st.write("Enter your password below to see how strong it is.")

    # Input box for the user's password
    user_password = st.text_input("Enter your password:", type="password")

    # Check the password when the user enters something
    if user_password:
        problems, score = evaluate_password(user_password)
        for problem in problems:
            st.write(problem)

        # If the password is weak, suggest a better one
        if score < 4:
            st.write("\n**No worries! Here's a strong password you can use:**")
            suggested_password = create_strong_password()
            st.code(suggested_password)

    # Button to generate a strong password
    if st.button("Generate a Strong Password"):
        new_password = create_strong_password()
        st.write("**Here's a strong password for you:**")
        st.code(new_password)

# Run the app
if __name__ == "__main__":
    main()