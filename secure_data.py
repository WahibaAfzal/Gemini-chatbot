import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import time

# Fixed key
KEY = b'PWzZ5wO58uWZ-KMCePVL3l5uvlzqoeK4fZpMQ_t-LPQ='
cipher = Fernet(KEY)

# Initialize session state
if "data" not in st.session_state:
    st.session_state["data"] = None

# Helper functions
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# UI
st.title("🔐 Simple Secure Data App")

menu = ["🏠 Home", "📥 Save Data", "📤 View Data"]
choice = st.sidebar.radio("Menu", menu)

if choice == "🏠 Home":
    st.info("Use this app to save a secret and retrieve it using a passkey.")

elif choice == "📥 Save Data":
    st.header("📥 Save Your Secret")
    secret = st.text_area("Write something secret:")
    passkey = st.text_input("Create a passkey", type="password")

    if st.button("Save"):
        if secret and passkey:
            encrypted = encrypt_data(secret)
            hashed_key = hash_passkey(passkey)
            st.session_state["data"] = {"encrypted": encrypted, "passkey": hashed_key}
            st.success("✅ Secret saved!")
        else:
            st.error("Please enter both secret and passkey!")

elif choice == "📤 View Data":
    st.header("📤 Retrieve Your Secret")
    passkey = st.text_input("Enter your passkey to view data", type="password")

    if st.button("Retrieve"):
        if st.session_state["data"]:
            stored_pass = st.session_state["data"]["passkey"]
            if hash_passkey(passkey) == stored_pass:
                with st.spinner("Decrypting..."):
                    time.sleep(1)
                original = decrypt_data(st.session_state["data"]["encrypted"])
                st.success("✅ Here is your secret:")
                st.code(original)
                st.snow()
            else:
                st.error("❌ Wrong passkey!")
        else:
            st.warning("⚠️ No data saved yet.")
