import streamlit as st
from utils.ai_match import find_matching_tutors

def show_student_dashboard():
    st.markdown("""
        <style>
        .main { background-color: #FFF7F2; }
        .welcome-text { font-size: 24px; font-weight: 600; color: #F4500A; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([6,1,1])
    with col1:
        st.markdown(f'<p class="welcome-text">Good morning, {st.session_state.email}!</p>', 
                    unsafe_allow_html=True)
        st.caption("Find a tutor, track your sessions, manage your profile.")
    with col3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")

    st.markdown("### 🤖 AI Tutor Match")
    query = st.text_input("Tell me what you need — subject, location, budget...", 
                          placeholder="e.g. I need a maths tutor near Velachery, offline, under ₹500/hr")
    
    if st.button("Find My Tutor ✨", use_container_width=True):
        if query:
            with st.spinner("AI is finding your best matches..."):
                result = find_matching_tutors(query)
                st.session_state.ai_result = result
        else:
            st.warning("Please tell us what you're looking for!")

    if "ai_result" in st.session_state:
        st.markdown("### 🎯 AI Recommended Tutors")
        st.markdown(st.session_state.ai_result)

    st.markdown("---")

    st.markdown("### Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("🔍 Find Tutor", use_container_width=True)
    with col2:
        st.button("✏️ Edit Profile", use_container_width=True)
    with col3:
        st.button("📅 My Sessions", use_container_width=True)
    with col4:
        st.button("❤️ Saved Tutors", use_container_width=True)

    st.markdown("---")

    st.markdown("### 🌟 Recommended Tutors")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="background:#fff; border: 2px solid #F4500A; 
                        border-radius:10px; padding:15px;">
                <h4>Rajesh Kumar</h4>
                <p>📚 Maths · Velachery · ₹400/hr</p>
                <p>🏷️ Offline · 12th · JEE</p>
                <p style="color:#F4500A; font-weight:600;">98% match</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Connect", key="t1", use_container_width=True)

    with col2:
        st.markdown("""
            <div style="background:#fff; border: 0.5px solid #ddd; 
                        border-radius:10px; padding:15px;">
                <h4>Priya Menon</h4>
                <p>📚 Maths · Adyar · ₹450/hr</p>
                <p>🏷️ Offline · Calculus</p>
                <p style="color:#F4500A; font-weight:600;">91% match</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Connect", key="t2", use_container_width=True)

    with col3:
        st.markdown("""
            <div style="background:#fff; border: 0.5px solid #ddd; 
                        border-radius:10px; padding:15px;">
                <h4>Suresh K.</h4>
                <p>📚 Physics · T.Nagar · ₹500/hr</p>
                <p>🏷️ Online · NEET</p>
                <p style="color:#F4500A; font-weight:600;">85% match</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Connect", key="t3", use_container_width=True)