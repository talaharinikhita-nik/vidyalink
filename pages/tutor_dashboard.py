import streamlit as st

def show_tutor_dashboard():
    st.markdown("""
        <style>
        .main { background-color: #FFF7F2; }
        .welcome-text { font-size: 24px; font-weight: 600; color: #F4500A; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([6,1,1])
    with col1:
        st.markdown(f'<p class="welcome-text">Welcome, {st.session_state.email}!</p>',
                    unsafe_allow_html=True)
        st.caption("Manage your students, update your profile, track requests.")
    with col3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")

    st.markdown("### 📊 Your Stats")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Students", "12")
    with col2:
        st.metric("New Requests", "3")
    with col3:
        st.metric("Sessions Done", "48")
    with col4:
        st.metric("Avg Rating", "4.9 ⭐")

    st.markdown("---")

    st.markdown("### Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("✏️ Edit Profile", use_container_width=True)
    with col2:
        st.button("📅 Availability", use_container_width=True)
    with col3:
        st.button("📄 My Info", use_container_width=True)
    with col4:
        st.button("📊 My Stats", use_container_width=True)

    st.markdown("---")

    st.markdown("### 📋 Student Requests")

    students = [
        {"name": "Ananya N.", "subject": "Maths", "mode": "Offline", 
         "location": "Velachery", "rate": "₹400/hr", "status": "Pending"},
        {"name": "Vikram R.", "subject": "Maths", "mode": "Online", 
         "location": "Adyar", "rate": "₹400/hr", "status": "Active"},
        {"name": "Sowmya K.", "subject": "Physics", "mode": "Offline", 
         "location": "T.Nagar", "rate": "₹450/hr", "status": "Active"},
    ]

    for student in students:
        col1, col2, col3 = st.columns([4, 2, 1])
        with col1:
            st.markdown(f"**{student['name']}**")
            st.caption(f"{student['subject']} · {student['mode']} · {student['location']} · {student['rate']}")
        with col2:
            if student['status'] == "Active":
                st.success("Active")
            else:
                st.warning("Pending")
        with col3:
            st.button("View", key=student['name'], use_container_width=True)
        st.divider()