
import streamlit as st
import random
import string
import re

# Function to evaluate password strength
def evaluate_password(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (@$!%*?&).")

    # Ensure score is within valid index range (0 to 4)
    score = min(score, 4)

    return score, feedback

# Function to generate a random secure password
def generate_password():
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit app settings
st.set_page_config(page_title="Secure Password Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")

# Initialize session state variables
if "generated_pass" not in st.session_state:
    st.session_state.generated_pass = ""
if "user_password" not in st.session_state:
    st.session_state.user_password = ""

# Button to generate a new password
if st.button("Generate Secure Password"):
    st.session_state.generated_pass = generate_password()

# Show generated password
if st.session_state.generated_pass:
    st.text_input("Generated Password:", st.session_state.generated_pass, disabled=True)

    # Button to use generated password
    if st.button("Use This Password"):
        st.session_state.user_password = st.session_state.generated_pass

# Password input field
password = st.text_input("Enter your password:", st.session_state.user_password, type="password")

# Password strength evaluation
if password:
    strength_labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength, suggestions = evaluate_password(password)

    st.subheader(f"Password Strength: {strength_labels[strength]}")
    st.progress(strength / 4)  # Normalize progress bar (0 to 1)

    if strength < 4:
        st.warning("Suggestions to improve:")
        for tip in suggestions:
            st.write(f"✅ {tip}")
    else:
        st.success("Great! Your password is secure.")
