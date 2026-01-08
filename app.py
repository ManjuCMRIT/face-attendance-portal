import streamlit as st

st.set_page_config(
    page_title="Face Attendance System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Face Attendance System")
st.caption("Role-based access portal")

st.divider()

st.markdown("### Select your role")

ADMIN_URL = "https://face-attendance-admin.streamlit.app"
STUDENT_URL = "https://face-registration-v2.streamlit.app"
TEACHER_URL = "https://face-attendance-v2.streamlit.app"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🧑‍💼 Admin")
    st.markdown(
        f"""
        <a href="{ADMIN_URL}" target="_self">
            <button style="width:100%;padding:10px;font-size:16px;">
                Admin Dashboard
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("#### 🧑‍🎓 Student")
    st.markdown(
        f"""
        <a href="{STUDENT_URL}" target="_self">
            <button style="width:100%;padding:10px;font-size:16px;">
                Face Registration
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown("#### 🧑‍🏫 Teacher")
    st.markdown(
        f"""
        <a href="{TEACHER_URL}" target="_self">
            <button style="width:100%;padding:10px;font-size:16px;">
                Take Attendance
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.caption(
    "This system uses AI-based face recognition for secure attendance management."
)
