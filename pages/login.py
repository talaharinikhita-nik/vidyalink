import streamlit as st

def show_login():
    st.markdown("""
        <style>
        .main { background-color: #FFF7F2; }
        .login-title { font-size: 32px; font-weight: 600; color: #F4500A; }
        .login-sub { font-size: 16px; color: #666; margin-bottom: 20px; }
        .privacy-note { background-color: #FEE8DC; padding: 10px 15px; 
                        border-radius: 8px; color: #B83400; font-size: 13px; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="login-title">Learn without limits.</p>', 
                    unsafe_allow_html=True)
        st.markdown('<p class="login-sub">India\'s privacy-first tutoring platform.<br>No Aadhaar. No PAN. Just learning.</p>', 
                    unsafe_allow_html=True)
        st.markdown("""
            <div class="privacy-note">
            🔒 We never ask for sensitive documents. 
            Only what's needed to connect you with the right tutor.
            </div>
        """, unsafe_allow_html=True)
        st.markdown("###")
        st.metric("Tutors", "2,400+")
        st.metric("Students", "8,100+")

    with col2:
        st.markdown("### Welcome to VidyaLink")
        role = st.radio("I am a", ["Student", "Tutor"], horizontal=True)
        email = st.text_input("Email or Phone")
        password = st.text_input("Password", type="password")

        if st.button("Sign In", use_container_width=True):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.email = email
                st.success(f"Welcome! Logging you in as {role}...")
                st.rerun()
            else:
                st.error("Please enter email and password")

        st.markdown("---")
        st.markdown("New here? Register below 👇")
        if st.button("Create Account", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()