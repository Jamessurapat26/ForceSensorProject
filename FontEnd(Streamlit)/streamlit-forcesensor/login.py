import streamlit as st

def login():
    # Create an empty container
    placeholder = st.empty()

    actual_email = "admin"
    actual_password = "root"

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### Welcome")
        email = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit and email == actual_email and password == actual_password:
        # If the form is submitted and the email and password are correct,
        # clear the form/container and return True
        placeholder.empty()
        return True
    elif submit and (email != actual_email or password != actual_password):
        st.error("Login failed")
        return False
    else:
        return False

if __name__ == "__main__":
    login()