# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to get Gemini response
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-3.5-flash-lite")

    if input_prompt != "":
        response = model.generate_content([input_prompt, image])
    else:
        response = model.generate_content(image)

    return response.text


# Streamlit App Configuration
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Image Application")

# User Input
input_prompt = st.text_input("Input Prompt:", key="input")

# Image Upload
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Button
submit = st.button("Tell me about the image")

# Generate Response
if submit:
    if image is None:
        st.warning("Please upload an image first.")
    else:
        response = get_gemini_response(input_prompt, image)
        st.subheader("The Response is:")
        st.write(response)