import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

def get_supabase():
    url = st.secrets.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
    key = st.secrets.get("SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")
    return create_client(url, key)

def save_tutor(name, email, phone, subjects, location, mode, rate, experience, classes):
    supabase = get_supabase()
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "subjects": subjects,
        "location": location,
        "mode": mode,
        "rate": rate,
        "experience": experience,
        "classes": classes
    }
    result = supabase.table("tutors").insert(data).execute()
    return result

def save_student(name, email, phone, subjects, location, mode, budget):
    supabase = get_supabase()
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "subjects": subjects,
        "location": location,
        "mode": mode,
        "budget": budget
    }
    result = supabase.table("students").insert(data).execute()
    return result

def get_all_tutors():
    supabase = get_supabase()
    result = supabase.table("tutors").select("*").execute()
    return result.data

def get_all_students():
    supabase = get_supabase()
    result = supabase.table("students").select("*").execute()
    return result.data

def report_user(reported_email, reason, reported_by):
    supabase = get_supabase()
    data = {
        "reported_email": reported_email,
        "reason": reason,
        "reported_by": reported_by
    }
    result = supabase.table("reports").insert(data).execute()
    return result