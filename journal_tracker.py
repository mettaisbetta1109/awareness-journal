import streamlit as st
import pandas as pd
import datetime

# Title
st.title("📝 Awareness in Action: Journaling & Transformation Tracker")

# Initialize session state for journal entries
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# User Input Section
st.header("Log Your Reflection")

date = st.date_input("📅 Select Date", datetime.date.today())
reflection = st.text_area("💡 Describe your 'aha' moment")

# Category Selection
st.subheader("🛠 Select Reflection Category")
categories = ["Emotional Shift", "Physical Sensation", "Habit Reinforcement", "Perspective Shift"]
selected_category = st.selectbox("📂 Choose a category", categories)

# Mood & Energy Tracking
st.subheader("🎭 Rate Your Experience")
mood = st.slider("😊 Mood Level (1-10)", 1, 10, 5)
energy = st.slider("⚡ Energy Level (1-10)", 1, 10, 5)

# Save Entry
if st.button("💾 Save Entry"):
    data_entry = {
        "Date": date,
        "Reflection": reflection,
        "Category": selected_category,
        "Mood": mood,
        "Energy": energy
    }
    st.session_state.journal_entries.append(data_entry)
    st.success("✅ Entry saved successfully!")

# Display Past Entries
if st.session_state.journal_entries:
    st.header("📖 Past Reflections")
    df = pd.DataFrame(st.session_state.journal_entries)
    st.dataframe(df)

    # Visualization of Mood & Energy Trends
    st.header("📊 Mood & Energy Trends Over Time")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date")
    st.line_chart(df.set_index("Date")[['Mood', 'Energy']])
