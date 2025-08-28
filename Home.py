import streamlit as st

st.set_page_config(
    page_title="LoveCare for the Needy Foundation",
    layout="wide",
)

# --- HERO Section ---
st.image(
    "children.jpg",
    caption="...",
    use_container_width=True
)

st.title("LoveCare for the Needy Foundation")
st.subheader("...")

st.write("""
LoveCare for the Needy Foundation is a registered non-profit organisation established in ...
""")

# --- Vision & Mission ---
st.header("Our Vision")
st.write("""
To build a .... society through ...
""")

st.header("Our Mission")
st.write("""
To Reach the destitute, handicapped, orphans, old widows/widowers.....
""")

# --- Who We Are ---
st.header("Who We Are")
st.write("""
Lovecare Foundation for the needy is a christian based NGO that takes care of the needy
""")

# --- Core Initiatives with Images ---
st.header("Our Core Initiatives")

col1, col2 = st.columns(2)

with col1:
    st.image("children.jpg", caption="...", use_container_width=True)
with col2:
    st.subheader("📚 To Reach Orphans")
    st.write("""
    .....
""")

col1, col2 = st.columns(2)

with col1:
    st.image("widow.jpg", caption="....", use_container_width=True)
with col2:
    st.subheader("🌾 To Reach old widows/widowers")
    st.write("""
    ......
""")

col1, col2 = st.columns(2)

with col1:
    st.image("disabled.jpg", caption=".....", use_container_width=True)
with col2:
    st.subheader("🤕 To Reach the handicapped/disabled")
    st.write("""
    ......
""")

# --- Our Events ---
st.header("Our Events")
st.write("""
Each year, the Foundation ......
""")

# --- Board of Trustees ---
st.header("Board of Trustees")

trustees = [
    {
"name": "Mr. Ojiakor Ifeomamebe",
"role": "Founder & Chairperson",
"bio": "........."
    },
    {
"name": "Mr. ...........",
"role": "..........",
"bio": "........"
    },
    {
"name": "Mrs. ...........",
"role": "...........",
"bio": "............."
    },
    {
"name": "Mr. ...........",
"role": "....................",
"bio": "................"
    },
    {
"name": "Mrs. ..........",
"role": "..........",
"bio": "..........."
    },
]

for trustee in trustees:
    st.subheader(f"{trustee['name']} — {trustee['role']}")
    st.write(trustee["bio"])

# --- Donate Button ---
st.header("Support Our Mission")
if st.button("💖 Donate Now"):
    st.write("Redirecting to donation page...")
    st.markdown("[Click here to donate](https://your_donation_link.com)")

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

st.info("© 2025 LoveCare for the Needy Foundation")
