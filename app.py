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

ADMIN_URL = "https://face-attendance-app-xt5yx9f8r5t3uygjft8qmj.streamlit.app/"
STUDENT_URL = "https://face-registration-v2-ssfuhbl72wtwhc3hb2qmse.streamlit.app/"
TEACHER_URL = "https://face-attendance-v2-d4tw52w5orezdevudep8xl.streamlit.app/"

st.markdown(f"""
### 🧑‍💼 Admin  
👉 [Open Admin Dashboard]({ADMIN_URL})

---

### 🧑‍🎓 Student  
👉 [Face Registration]({STUDENT_URL})

---

### 🧑‍🏫 Teacher  
👉 [Take Attendance]({TEACHER_URL})
""")

st.divider()

st.caption(
    "AI-powered face recognition system for secure academic attendance management."
)
