# Q&A Chatbot
#from langchain.llms import OpenAI
import streamlit as st

st.write("NEW VERSION LOADED")

from dotenv import load_dotenv
import streamlit as st
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Gemini Chatbot")
st.title("Gemini Chatbot")

question = st.text_input("Ask a question")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question,
    )
    st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")