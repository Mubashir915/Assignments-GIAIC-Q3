import streamlit as st
from random import choice as pick_one
from datetime import date
import os

# Page config
st.set_page_config(
    page_title="Mindset Helper", 
    page_icon="✨",
    layout="centered"
)

# Styling
st.markdown("""
<style>
.bubble {
    background: #f5f9ff;
    padding: 15px;
    border-radius: 12px;
    margin: 12px 0;
    border-left: 4px solid #6c9eff;
}
.good {
    color: #2e7d32;
}
.reminder {
    color: #d32f2f;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 Growth Mindset Helper")

st.write("""
Welcome! This space helps you reflect, grow, and develop a positive mindset — one small step at a time.
""")

# ---- THOUGHT OF THE DAY ----
st.header("🌟 Today's Thought")
daily_thoughts = [
    "Every expert was once a beginner.",
    "Small steps still move you forward.",
    "Mistakes are just learning in disguise.",
    "Progress beats perfection every time.",
    "You're closer today than yesterday."
]
thought = pick_one(daily_thoughts)
st.markdown(f'<div class="bubble">"{thought}"</div>', unsafe_allow_html=True)

# ---- MOOD TRACKER ----
st.header("🧠 How Are You Feeling Today?")
mood = st.selectbox("Pick a mood that fits:", ["😊 Happy", "😐 Neutral", "😟 Sad", "😡 Frustrated", "😌 Calm"])
st.write("It's okay to feel however you feel today. Noticing is the first step.")

# ---- REFLECTION ----
st.header("💭 Quick Reflection")
st.write("How true does this feel for you today?")
st.write("'I can get better at things with practice.'")

user_feeling = st.radio(
    "Your answer:",
    ("Very true", "Mostly true", "Not sure", "Not very true", "Not true at all"),
    index=2,
    horizontal=True
)

if user_feeling:
    st.write("You chose:", user_feeling)
    if user_feeling in ["Very true", "Mostly true"]:
        st.markdown("<span class='good'>That's a great way to think!</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='reminder'>Remember - every skill was learned by someone!</span>", unsafe_allow_html=True)

# ---- GRATITUDE JOURNAL ----
st.header("🙏 Gratitude Journal")
gratitude = st.text_area("Write down one thing you're thankful for today:")

# ---- PRACTICAL TIP ----
st.header("🔧 Try This Today")
helpful_tips = [
    "Notice one thing you improved at recently.",
    "Say 'I'm learning' instead of 'I can't'.",
    "Pick one small thing to practice today.",
    "Thank someone who helped you learn.",
    "Write down something new you learned."
]
st.write(pick_one(helpful_tips))

# ---- DAILY STREAK TRACKER ----
st.header("🔥 Daily Streak")
streak_key = "streak"
last_check_in_key = "last_check_in"

if streak_key not in st.session_state:
    st.session_state[streak_key] = 0
    st.session_state[last_check_in_key] = None

today = str(date.today())
if st.session_state[last_check_in_key] != today:
    st.session_state[streak_key] += 1
    st.session_state[last_check_in_key] = today

st.success(f"You're on a **{st.session_state[streak_key]} day** streak! Keep it up!")

# ---- JOURNAL EXPORT ----
st.header("📥 Save Today's Reflection")
if st.button("📄 Download Summary"):
    filename = f"Mindset_Journal_{today}.txt"
    summary = f"""
Date: {today}
Thought of the Day: {thought}
Mood: {mood}
Reflection: {user_feeling}
Gratitude: {gratitude if gratitude else 'Not entered.'}
Daily Tip: {pick_one(helpful_tips)}
Streak: {st.session_state[streak_key]} days
"""
    with open(filename, "w") as f:
        f.write(summary)
    with open(filename, "rb") as f:
        st.download_button("Download", f, file_name=filename)
    os.remove(filename)

# ---- FOOTER ----
st.markdown("---")
st.write("💡 Remember: Growth is a journey, not a race. Keep going ❤️")
