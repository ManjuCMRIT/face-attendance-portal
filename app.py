import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Face Attendance System",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🎓 Face Attendance System</h1>
    <p style="text-align:center; font-size:16px; color:gray;">
        AI-powered, role-based attendance management
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# INTRO
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; font-size:15px;">
        This system provides <b>secure face-based attendance</b> through 
        dedicated portals for <b>Admin</b>, <b>Students</b>, and <b>Teachers</b>.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# URLs (YOUR DEPLOYED APPS)
# --------------------------------------------------
ADMIN_URL = "https://face-attendance-app-xt5yx9f8r5t3uygjft8qmj.streamlit.app/"
STUDENT_URL = "https://face-registration-v2-ssfuhbl72wtwhc3hb2qmse.streamlit.app/"
TEACHER_URL = "https://face-attendance-v2-d4tw52w5orezdevudep8xl.streamlit.app/"

# --------------------------------------------------
# ROLE CARDS
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            border:1px solid #e0e0e0;
            border-radius:10px;
            padding:20px;
            text-align:center;
        ">
            <h3>🧑‍💼 Admin</h3>
            <p style="font-size:14px;">
                Manage classes, students, and system configuration
            </p>
            <a href="{0}" target="_blank">
                <button style="
                    width:100%;
                    padding:10px;
                    background-color:#4CAF50;
                    color:white;
                    border:none;
                    border-radius:6px;
                    font-size:15px;
                    cursor:pointer;
                ">
                    Open Admin Dashboard
                </button>
            </a>
        </div>
        """.format(ADMIN_URL),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            border:1px solid #e0e0e0;
            border-radius:10px;
            padding:20px;
            text-align:center;
        ">
            <h3>🧑‍🎓 Student</h3>
            <p style="font-size:14px;">
                Register your face securely using your USN
            </p>
            <a href="{0}" target="_blank">
                <button style="
                    width:100%;
                    padding:10px;
                    background-color:#2196F3;
                    color:white;
                    border:none;
                    border-radius:6px;
                    font-size:15px;
                    cursor:pointer;
                ">
                    Face Registration
                </button>
            </a>
        </div>
        """.format(STUDENT_URL),
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="
            border:1px solid #e0e0e0;
            border-radius:10px;
            padding:20px;
            text-align:center;
        ">
            <h3>🧑‍🏫 Teacher</h3>
            <p style="font-size:14px;">
                Take attendance and generate reports
            </p>
            <a href="{0}" target="_blank">
                <button style="
                    width:100%;
                    padding:10px;
                    background-color:#FF9800;
                    color:white;
                    border:none;
                    border-radius:6px;
                    font-size:15px;
                    cursor:pointer;
                ">
                    Take Attendance
                </button>
            </a>
        </div>
        """.format(TEACHER_URL),
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.markdown(
    """
    <div style="text-align:center; font-size:13px; color:gray;">
        Developed as an academic AI system for face recognition–based attendance<br>
        Department of CSE • CMRIT
    </div>
    """,
    unsafe_allow_html=True
)
