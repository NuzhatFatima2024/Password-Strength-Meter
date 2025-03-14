import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    
    # Check length of the password
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # Check for lowercase, uppercase, and digits
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    
    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    
    # Return a string based on the score
    if score <= 2:
        return "Weak", "red"
    elif score == 3:
        return "Medium", "orange"
    elif score == 4:
        return "Strong", "yellowgreen"
    else:
        return "Very Strong", "green"

# Streamlit UI
st.title("Password Strength Meter")

# User input for password
password = st.text_input("Enter a password", type="password")

# Check password strength
if password:
    strength, color = check_password_strength(password)
    
    # Display the strength and meter
    st.write(f"Password Strength: **{strength}**")
    st.markdown(f"<div style='background-color:{color}; padding:10px; color:white; font-weight:bold; text-align:center;'> {strength} </div>", unsafe_allow_html=True)
else:
    st.write("Enter a password to check its strength.")

# Add some styling for the app
st.markdown("""
    <style>
        .stTextInput input {
            font-size: 18px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .stButton>button {
            font-size: 18px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
        }
        .stTitle {
            font-size: 32px;
        }
    </style>
""", unsafe_allow_html=True)
