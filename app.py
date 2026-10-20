import streamlit as st

import auth

user = auth.current_user()

if user is None:
    st.title("Sign in")
else:
    st.title("Home")
    st.write(f"Welcome, {user.name}")
    st.button("Sign out", on_click=auth.sign_out)
