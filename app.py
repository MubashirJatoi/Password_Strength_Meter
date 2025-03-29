import streamlit as st
import re
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("Password Strength Meter")
st.markdown("## Create your Strongest password!")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "1234", "qwerty", 
    "letmein", "admin", "welcome", "password1", "abc123"
]



if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password must be atleast 8 character")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password must contain both upper and lower case characters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password must contain atleast one digit")

    if re.search(r'[!@#$%^_-]', password):
        score += 1
    else:
        feedback.append("❌Password must contain atleast one special character(!@#$%^_-).")

    if score == 4:
        feedback.append("✅Your password is strong!")
    elif score == 3:
        feedback.append("😐Your password is medium strength. it could be stronger.")
    else:
        feedback.append("👎Your password is weak. Please make it stronger.")

    if feedback:
        st.markdown("## Improvment suggestions")
        for tips in feedback:
            st.write(tips)

else:
    st.info("Please enter your password to get started.")
