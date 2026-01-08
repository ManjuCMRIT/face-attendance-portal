import streamlit as st

st.set_page_config(
    page_title="Face Attendance System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Face Attendance System")
st.caption("Unified portal for Admin, Student, and Teacher")

st.divider()

st.markdown("### Select your role")

# ✅ YOUR ACTUAL DEPLOYED URLs
ADMIN_URL = "https://face-attendance-app-xt5yx9f8r5t3uygjft8qmj.streamlit.app/"
STUDENT_URL = "https://face-registration-v2-ssfuhbl72wtwhc3hb2qmse.streamlit.app/"
TEACHER_URL = "https://face-attendance-v2-d4tw52w5orezdevudep8xl.streamlit.app/"

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧑‍💼 Admin")
    st.link_button(
        "Open Admin Dashboard",
        ADMIN_URL,
        use_container_width=True
    )

with col2:
    st.subheader("🧑‍🎓 Student")
    st.link_button(
        "Register Face",
        STUDENT_URL,
        use_container_width=True
    )

with col3:
    st.subheader("🧑‍🏫 Teacher")
    st.link_button(
        "Take Attendance",
        TEACHER_URL,
        use_container_width=True
    )

st.divider()

st.caption(
    "AI-powered face recognition system for secure academic attendance management."
)
