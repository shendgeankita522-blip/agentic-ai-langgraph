from dotenv import load_dotenv
import streamlit as st
import os
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Streamlit UI
st.set_page_config(page_title="Gemini Q&A Chatbot")
st.title("Gemini Q&A Chatbot")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input
question = st.text_input("Ask your question")

# Button
if st.button("Ask") and question:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question,
        )

        answer = response.text

        st.session_state.history.append(("You", question))
        st.session_state.history.append(("Bot", answer))

        st.success(answer)

    except Exception as e:
        st.error(str(e))

# Chat History
st.subheader("Chat History")

for role, text in st.session_state.history:
    st.write(f"**{role}:** {text}")