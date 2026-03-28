import streamlit as st
from groq import Groq
from datetime import datetime
import pytz

# --- Groq API ---
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Smart Study Planner 📚")
st.write("Generate a study plan that prioritises the hardest chapters first.")

# --- Timezone Selection ---
timezone_option = st.selectbox(
    "Select your timezone",
    ["IST (India)", "EST (US East)"]
)

# Convert timezone
if timezone_option == "IST (India)":
    tz = pytz.timezone("Asia/Kolkata")
else:
    tz = pytz.timezone("US/Eastern")

current_time = datetime.now(tz)

st.write("Current Date:", current_time.strftime("%Y-%m-%d"))
st.write("Current Time:", current_time.strftime("%I:%M %p"))

# --- Inputs ---
subjects = st.text_input(
    "Enter your subjects",
    placeholder="Example: Math, Physics, Chemistry"
)

chapters = st.text_area(
    "Enter chapters for each subject",
    placeholder="Example:\nMath: Algebra, Trigonometry\nPhysics: Electricity\nChemistry: Organic Chemistry"
)

hardest = st.text_input(
    "Which chapters are the hardest?",
    placeholder="Example: Trigonometry, Electricity"
)

exam_date = st.date_input("Enter exam date")

hours = st.number_input(
    "How many hours can you study per day?",
    min_value=1,
    max_value=12
)

# --- Generate Plan ---
if st.button("Generate Study Plan"):

    prompt = f"""
    Create a day-by-day study plan for a student.

    Subjects: {subjects}

    Chapters:
    {chapters}

    Hardest chapters:
    {hardest}

    Current date: {current_time.strftime("%Y-%m-%d")}
    Current time: {current_time.strftime("%I:%M %p")}
    Timezone: {timezone_option}

    Exam date: {exam_date}

    Study hours per day: {hours}

    Instructions:
    - Start studying from the current time today.
    - Prioritise the hardest chapters first.
    - Leave easier chapters later.
    - Spread the chapters until the exam date.
    - Make the plan clear and organised day by day.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    plan = response.choices[0].message.content

    st.subheader("Your AI Study Plan 📅")
    st.write(plan)