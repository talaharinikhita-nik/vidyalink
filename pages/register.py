import streamlit as st
from utils.database import save_tutor, save_student

def show_register():
    st.markdown("""
        <style>
        .main { background-color: #FFF7F2; }
        .reg-title { font-size: 28px; font-weight: 600; color: #F4500A; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="reg-title">Create your VidyaLink account</p>', 
                unsafe_allow_html=True)
    st.markdown("""
        <div style="background:#FEE8DC; padding:10px 15px; border-radius:8px; 
                    color:#B83400; font-size:13px; margin-bottom:20px;">
        🔒 No Aadhaar. No PAN. No sensitive documents required.
        </div>
    """, unsafe_allow_html=True)

    role = st.radio("I am a", ["Student", "Tutor"], horizontal=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        location = st.text_input("Area / Location (e.g. Velachery, Chennai)")
    with col2:
        subjects = st.text_input("Subjects (e.g. Maths, Physics)")
        mode = st.selectbox("Preferred Mode", ["Online", "Offline", "Both"])
        if role == "Tutor":
            rate = st.number_input("Your Rate (₹/hr)", min_value=100, max_value=5000, value=400)
            experience = st.text_input("Experience (e.g. 3 years)")
            classes = st.text_input("Classes you teach (e.g. 10th-12th, JEE)")
        else:
            budget = st.number_input("Your Budget (₹/hr)", min_value=100, max_value=5000, value=300)

    st.markdown("---")

    if st.button("Create Account", use_container_width=True):
        if not name or not email or not phone or not location or not subjects:
            st.error("Please fill in all fields!")
        elif len(phone) != 10 or not phone.isdigit():
            st.error("Please enter a valid 10-digit phone number!")
        else:
            try:
                if role == "Tutor":
                    save_tutor(name, email, phone, subjects, 
                              location, mode, rate, experience, classes)
                else:
                    save_student(name, email, phone, subjects, 
                                location, mode, budget)
                st.success(f"Welcome to VidyaLink, {name}! Account created successfully!")
                st.balloons()
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.email = email
                st.rerun()
            except Exception as e:
                st.error(f"Error creating account: {str(e)}")

    st.markdown("---")
    if st.button("Already have an account? Sign In", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()