import streamlit as st
from dotenv import load_dotenv
import os
from pages.login import show_login
from pages.register import show_register
from pages.student_dashboard import show_student_dashboard
from pages.tutor_dashboard import show_tutor_dashboard

load_dotenv()

st.set_page_config(
    page_title="VidyaLink",
    page_icon="📚",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

if not st.session_state.logged_in:
    if st.session_state.page == "register":
        show_register()
    else:
        show_login()
else:
    if st.session_state.role == "Student":
        show_student_dashboard()
    else:
        show_tutor_dashboard()