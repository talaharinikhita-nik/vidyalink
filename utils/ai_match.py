import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tutors = [
    {"name": "Rajesh Kumar", "subject": "Maths", "location": "Velachery", 
     "mode": "Offline", "rate": 400, "experience": "5 years", "classes": "10th-12th, JEE"},
    {"name": "Priya Menon", "subject": "Maths", "location": "Adyar", 
     "mode": "Offline", "rate": 450, "experience": "3 years", "classes": "Calculus"},
    {"name": "Suresh K.", "subject": "Physics", "location": "T.Nagar", 
     "mode": "Online", "rate": 500, "experience": "7 years", "classes": "NEET"},
    {"name": "Divya S.", "subject": "Chemistry", "location": "Velachery", 
     "mode": "Both", "rate": 350, "experience": "4 years", "classes": "11th-12th, NEET"},
    {"name": "Arun M.", "subject": "Maths", "location": "Tambaram", 
     "mode": "Online", "rate": 300, "experience": "2 years", "classes": "6th-10th"},
]

def find_matching_tutors(query):
    tutor_list = "\n".join([
        f"- {t['name']}: {t['subject']}, {t['location']}, {t['mode']}, "
        f"₹{t['rate']}/hr, {t['experience']} exp, {t['classes']}"
        for t in tutors
    ])

    prompt = f"""
You are a tutor matching assistant for VidyaLink, an Indian tutoring platform.

A student is looking for: "{query}"

Here are the available tutors:
{tutor_list}

Based on the student's request, pick the TOP 3 best matching tutors and explain in 1 line why each is a good match.

Reply in this exact format for each tutor:
1. [Tutor Name] - [Match %] - [Reason]
2. [Tutor Name] - [Match %] - [Reason]
3. [Tutor Name] - [Match %] - [Reason]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content