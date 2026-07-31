# agentic-ai-langgraph
A collection of Agentic AI projects built using LangGraph, LangChain, Python, and LLMs, featuring stateful workflows, tool calling, memory, and intelligent AI agents.

# 🤖 Gemini AI Applications using Google Gemini API

## 📌 Overview

This repository contains multiple AI applications built using **Google Gemini API** and **Python**.
The project demonstrates different capabilities of Generative AI, including AI chatbot, question answering, image understanding, and Gemini model testing.

---

# 🚀 Applications Included

## 1. 💬 Gemini Chat Application

### File:

`chat.py`

### Description:

A conversational AI chatbot that uses the Google Gemini API to generate human-like responses.

### Features:

* Text-based AI conversation
* Natural language understanding
* Real-time Gemini responses

### Output:

![Gemini Chat Output]https://github.com/shendgeankita522-blip/agentic-ai-langgraph/blob/main/Images/Output%20Images/Vision1.png

---

# 2. ❓ Gemini Question Answering System

### File:

`qachat.py`

### Description:

A Question Answering application where users can ask questions and receive AI-generated answers using Gemini.

### Features:

* User query handling
* Context-based responses
* AI-powered question answering

### Output:

![Gemini QA Output](images/qachat_output.png)

---

# 3. 👁️ Gemini Vision Application

### File:

`vision.py`

### Description:

An image analysis application using Gemini Vision.
Users can upload images and ask questions about the image.

### Features:

* Image upload support
* Image understanding
* Visual question answering
* AI-generated image descriptions

## Input Image:

![Vision Input Image](images/vision_input.png)

## Gemini Vision Output:

![Vision Output](images/vision_output.png)

---

# 4. 🧪 Gemini Model Testing

### File:

`testmodels.py`

### Description:

This file is used to test Gemini models and verify API connectivity and model responses.

### Output:

![Model Testing Output](images/testmodel_output.png)

---

# 5. 📚 Gemini Introduction

### File:

`gemini_intro.py`

### Description:

Basic implementation of Google Gemini API with Python.

### Concepts Covered:

* Gemini API setup
* Model configuration
* Text generation

### Output:

![Gemini Intro Output](images/gemini_intro_output.png)

---

# 6. 📚 Gemini Introduction 1

### File:

`gemini_intro1.py`

### Description:

Additional examples demonstrating Gemini API usage and response generation.

### Output:

![Gemini Intro 1 Output](images/gemini_intro1_output.png)

---

# 🌐 Main Application

### File:

`app.py`

### Description:

Streamlit-based interface that combines Gemini AI features into a user-friendly web application.

### Features:

* Interactive UI
* Gemini-powered responses
* Easy user interaction

### Output:

![Streamlit App Output](images/app_output.png)

---

# 🛠️ Technologies Used

* Python
* Google Gemini API
* Streamlit
* Google Generative AI
* Python-dotenv
* Pillow

---

# 📂 Project Structure

```text
Gemini-AI-Applications/
│
├── app.py
├── chat.py
├── qachat.py
├── vision.py
├── testmodels.py
├── gemini_intro.py
├── gemini_intro1.py
│
├── images/
│   ├── Input.png
│   ├── Output.png
│   ├── 
│   ├── 
│   ├── 
│   ├
│   ├── 
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone <your-github-repository-url>
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key Setup

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Load the API key using:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
```

---

# ▶️ Run Application

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# ⚠️ Important Notes

* Never upload your `.env` file to GitHub.
* Keep your Gemini API key private.
* Add `.env` to `.gitignore`.
* Use your own Gemini API key before running the project.

---

# 🎯 Future Improvements

* Add conversation memory
* Add voice input/output
* Deploy using Streamlit Cloud
* Add more Gemini multimodal features

---

# 👩‍💻 Author

**Ankita Shendge**

B.Tech Artificial Intelligence & Data Science

GitHub: <your-github-profile-link>

LinkedIn: <your-linkedin-profile-link>

