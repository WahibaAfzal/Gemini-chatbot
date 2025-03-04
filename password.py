



# import streamlit as st
# import re
# import random
# import string

# # Function to generate a strong random password
# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + "!@#$%^&*()"
#     return ''.join(random.choice(characters) for _ in range(length))

# # Function to check password strength
# def check_password_strength(password):
#     strength = 0
#     suggestions = []
    
#     # Criteria checks
#     if len(password) >= 8:
#         strength += 1
#     else:
#         suggestions.append("Increase password length to at least 8 characters.")
    
#     if re.search(r"[A-Z]", password):
#         strength += 1
#     else:
#         suggestions.append("Add at least one uppercase letter.")
    
#     if re.search(r"[a-z]", password):
#         strength += 1
#     else:
#         suggestions.append("Add at least one lowercase letter.")
    
#     if re.search(r"\d", password):
#         strength += 1
#     else:
#         suggestions.append("Include at least one number.")
    
#     if re.search(r"[@$!%*?&]", password):
#         strength += 1
#     else:
#         suggestions.append("Use at least one special character (@$!%*?&).")
    
#     return strength, suggestions

# # Streamlit UI
# st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
# st.title("🔐 Password Strength Meter")
# st.markdown("Enter a password to check its strength! 🔽")

# # Store generated password in session state
# if "generated_password" not in st.session_state:
#     st.session_state.generated_password = ""

# if "use_generated_password" not in st.session_state:
#     st.session_state.use_generated_password = False

# # Use generated password in the main input
# if st.session_state.use_generated_password:
#     password = st.text_input("Enter Password:", value=st.session_state.generated_password, type="password", key="password_input")
# else:
#     password = st.text_input("Enter Password:", type="password", key="password_input")

# # Generate password section
# st.subheader("🔑 Generate a Strong Password")

# col1, col2 = st.columns(2)

# if col1.button("🔄 Generate Password"):
#     st.session_state.generated_password = generate_password()
#     st.session_state.use_generated_password = False  # Reset flag when a new password is generated

# # Show the generated password only if it exists
# if st.session_state.generated_password:
#     st.text_input("Generated Password:", value=st.session_state.generated_password, disabled=True)
    
#     # Show "Use This Password" button **only if a password is generated**
#     if col2.button("✅ Use This Password"):
#         st.session_state.use_generated_password = True  # Set flag to use generated password

# # Process password strength
# if password:
#     strength, suggestions = check_password_strength(password)
    
#     # Strength Levels
#     strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
#     # Fix the indexing issue
#     strength_index = min(strength, 4)  # Ensures valid index

#     # Display Strength
#     st.subheader(f"Strength: {strength_levels[strength_index]}")
#     st.progress(strength / 5)  # Show visual strength bar
    
#     # Suggest improvements
#     if strength < 5:
#         st.warning("💡 Suggestions to Improve:")
#         for s in suggestions:
#             st.write(f"✅ {s}")
#     else:
#         st.success("🎉 Great! Your password is very strong.")













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
