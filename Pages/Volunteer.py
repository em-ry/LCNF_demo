import streamlit as st

# --- Volunteer Sign-Up Form ---
st.header("Volunteer Sign-Up")

with st.form("volunteer_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number (Optional)")
    message = st.text_area("Tell us how you'd like to help")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thank you {name}! We will get back to you soon.")
