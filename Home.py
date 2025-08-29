import streamlit as st

st.set_page_config(
    page_title="LoveCare for the Needy Foundation",
    layout="wide",
)
dummy = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, " \
        "magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna."

# --- HERO Section ---
col1, col2 = st.columns(2)

with col1:
    st.image(
        "images/intro_img.jpg",
        caption="...",
        width="stretch"
    )
with col2:
    st.title("LOVECARE FOR THE NEEDY FOUNDATION")
    st.info(dummy)

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
    st.image("images/children.jpg", caption="...", width="stretch")
with col2:
    st.subheader("📚 To Reach Orphans")
    st.write(f"""
    {dummy}
""")

col1, col2 = st.columns(2)

with col1:
    st.image("images/widow.jpg", caption="....", width="stretch")
with col2:
    st.subheader("🌾 To Reach old widows/widowers")
    st.write(f"""
    {dummy}
""")

col1, col2 = st.columns(2)

with col1:
    st.image("images/disabled.jpg", caption=".....", width="stretch")
with col2:
    st.subheader("🤕 To Reach the handicapped/disabled")
    st.write(f"""
    {dummy}
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
        "bio": f"{dummy}"
    },
    {
        "name": "Mr. Anonymous",
        "role": "Unknown",
        "bio": f"{dummy}"
    },
    {
        "name": "Mrs. Anonymous",
        "role": "Unknown",
        "bio": f"{dummy}"
    },
    {
        "name": "Mr. Anonymous",
        "role": "Unknown",
        "bio": f"{dummy}"
    },
    {
        "name": "Mrs. Anonymous",
        "role": "Unkown",
        "bio": f"{dummy}"
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

st.info("© 2025 LoveCare for the Needy Foundation")
