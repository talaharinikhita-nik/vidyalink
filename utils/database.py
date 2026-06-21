import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(url, key)

def save_tutor(name, email, phone, subjects, location, mode, rate, experience, classes):
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
    result = supabase.table("tutors").select("*").execute()
    return result.data

def get_all_students():
    result = supabase.table("students").select("*").execute()
    return result.data

def report_user(reported_email, reason, reported_by):
    data = {
        "reported_email": reported_email,
        "reason": reason,
        "reported_by": reported_by
    }
    result = supabase.table("reports").insert(data).execute()
    return result