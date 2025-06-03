# A simple app to encourage positive thinking
import streamlit as st
from random import choice as pick_one

# Make the page look nice
st.set_page_config(
    page_title="Mindset Helper", 
    page_icon="✨",
    layout="centered"
)

# Some colors to make it friendly
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

# The main heading
st.title("🚀 Growth Mindset Challenge: Web App With Streamlit")
st.write("""
This web page helps remind us that we can always 
grow and improve with practice and effort.
""")

# Thought of the day section
st.header("Today's Thought")
daily_thoughts = [
    "Every expert was once a beginner",
    "Small steps still move you forward",
    "Mistakes are just learning in disguise",
    "Progress beats perfection every time",
    "You're closer today than yesterday"
]
thought = pick_one(daily_thoughts)
st.markdown(f'<div class="bubble">"{thought}"</div>', unsafe_allow_html=True)

# Quick reflection question
st.header("Quick Reflection")
st.write("How true does this feel for you today?")
st.write("'I can get better at things with practice'")

user_feeling = st.radio(
    "Your answer:",
    ("Very true", "Mostly true", "Not sure", 
     "Not very true", "Not true at all"),
    index=2,
    horizontal=True
)

# Response based on answer
if user_feeling:
    st.write("You chose:", user_feeling)
    if user_feeling in ["Very true", "Mostly true"]:
        st.markdown("<span class='good'>That's a great way to think!</span>", 
                   unsafe_allow_html=True)
    else:
        st.markdown("""<span class='reminder'>
        Remember - every skill was learned by someone!
        </span>""", unsafe_allow_html=True)

# Practical tip
st.header("Try This Today")
helpful_tips = [
    "Notice one thing you improved at recently",
    "Say 'I'm learning' instead of 'I can't'",
    "Pick one small thing to practice today",
    "Thank someone who helped you learn",
    "Write down something new you learned"
]
st.write(pick_one(helpful_tips))

# Closing
st.markdown("---")
st.write("Keep believing in growth❤️")