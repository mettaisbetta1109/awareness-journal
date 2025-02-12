import streamlit as st
import pandas as pd
import datetime
import os

# 🎨 Custom Styling
st.set_page_config(page_title="Awareness in Action", page_icon="✨", layout="centered")

# Define CSV File Location
CSV_FILE = "journal_entries.csv"

# Load Existing Data
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["Date", "Reflection", "Category", "Mood", "Energy"])

# 🌿 Custom CSS for Styling
st.markdown(
    """
    <style>
        .title { text-align: center; font-size: 2rem; color: #2A7F62; font-weight: bold; }
        .subtitle { text-align: center; font-size: 1.2rem; color: #555; }
        .stTextInput, .stTextArea, .stSelectbox, .stSlider {
            border-radius: 10px; padding: 8px; font-size: 1rem;
        }
        .stButton button { background-color: #2A7F62; color: white; font-weight: bold; padding: 10px; border-radius: 8px; }
        .stButton button:hover { background-color: #205D47; }
        .stMarkdown { font-size: 1rem; color: #444; }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎭 Title & Intro
st.markdown("<h1 class='title'>📝 Awareness in Action</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Track your reflections and watch your transformation unfold.</p>", unsafe_allow_html=True)
st.write("---")  # Divider

# 📅 Log Reflection - Use Two Columns for Layout
col1, col2 = st.columns(2)

with col1:
    date = st.date_input("📅 Select Date", datetime.date.today())
    selected_category = st.selectbox("📂 Choose a category", ["Emotional Shift", "Physical Sensation", "Habit Reinforcement", "Perspective Shift"])

with col2:
    mood = st.slider("😊 Mood Level (1-10)", 1, 10, 5)
    energy = st.slider("⚡ Energy Level (1-10)", 1, 10, 5)

reflection = st.text_area("💡 Describe your 'aha' moment")

# 💾 Save Entry (Now Saves to CSV File)
if st.button("💾 Save Entry"):
    new_entry = {"Date": date, "Reflection": reflection, "Category": selected_category, "Mood": mood, "Energy": energy}
    
    # Append the new entry to the DataFrame
    df = df.append(new_entry, ignore_index=True)
    
    # Save DataFrame to CSV
    df.to_csv(CSV_FILE, index=False)
    
    st.success("✅ Entry saved successfully! (Now stored permanently!)")

st.write("---")  # Divider

# 📖 Display Past Entries
if not df.empty:
    st.markdown("<h2 class='title'>📖 Past Reflections</h2>", unsafe_allow_html=True)
    st.dataframe(df)

    # 📊 Mood & Energy Trends Over Time
    st.markdown("<h2 class='title'>📊 Mood & Energy Trends Over Time</h2>", unsafe_allow_html=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date")
    st.line_chart(df.set_index("Date")[['Mood', 'Energy']])
