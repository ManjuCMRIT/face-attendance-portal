import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Intelli-Attendance App",
    page_icon="🎓",
    layout="centered"
)

# ==================================================
# LOGO
# ==================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/logocmrit.png", width=160)

# ==================================================
# TITLE & TAGLINE
# ==================================================
st.markdown(
    """
    <h1 style="text-align:center; margin-bottom:0;">
        Intelli-Attendance App
    </h1>
    <p style="text-align:center; font-size:16px; color:gray;">
        AI-Powered Face Recognition Attendance System
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# DESCRIPTION
# ==================================================
st.markdown(
    """
    <div style="text-align:center; font-size:15px;">
        A smart, secure, and scalable attendance system developed at  
        <b>CMR Institute of Technology, Bengaluru</b>.
        <br><br>
        This system enables accurate face-based attendance with  
        administrative control and manual verification.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# NAVIGATION BUTTONS
# ==================================================
st.subheader("🔗 Open Module")

ADMIN_URL = "https://face-attendance-app-xt5yx9f8r5t3uygjft8qmj.streamlit.app/"
ATTENDANCE_URL = "https://face-attendance-v2-d4tw52w5orezdevudep8xl.streamlit.app/"
REGISTRATION_URL = "https://face-registration-v2-ssfuhbl72wtwhc3hb2qmse.streamlit.app/"

colA, colB, colC = st.columns(3)

with colA:
    st.markdown(
        f"""
        <a href="{ADMIN_URL}" target="_blank">
            <button style="width:100%; height:60px; font-size:16px;">
                🛠 Admin Dashboard
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with colB:
    st.markdown(
        f"""
        <a href="{REGISTRATION_URL}" target="_blank">
            <button style="width:100%; height:60px; font-size:16px;">
                📸 Face Registration
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with colC:
    st.markdown(
        f"""
        <a href="{ATTENDANCE_URL}" target="_blank">
            <button style="width:100%; height:60px; font-size:16px;">
                🧑‍🏫 Take Attendance
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ==================================================
# FOOTER
# ==================================================
st.markdown(
    """
    <div style="text-align:center; font-size:13px; color:gray;">
        Developed as part of Mega Project (MEP) <br>
        © CMR Institute of Technology
    </div>
    """,
    unsafe_allow_html=True
)
