import streamlit as st
from utils import generate_learning_path

st.set_page_config(
    page_title="Learning Path Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI-Powered Learning Path Generator")

st.markdown(
    "Enter your learning goal and get a personalized roadmap powered by Gemini AI."
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")

    api_key = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="Paste your Gemini API key"
    )

# Main Input
goal = st.text_area(
    "What do you want to learn?",
    placeholder="Example: I want to learn Python in 5 days",
    height=120
)

# Generate Button
if st.button("🚀 Generate Learning Path", type="primary"):

    if not api_key:
        st.error("Please enter your Gemini API key.")
        st.stop()

    if not goal.strip():
        st.error("Please enter a learning goal.")
        st.stop()

    try:
        with st.spinner("Generating roadmap..."):

            result = generate_learning_path(
                goal=goal,
                api_key=api_key
            )

        st.success("Learning path generated successfully!")

        st.markdown("---")
        st.markdown(result)

    except Exception as e:
        st.error(f"Error: {str(e)}")