# agentic-ai-langgraph
A collection of Agentic AI projects built using LangGraph, LangChain, Python, and LLMs, featuring stateful workflows, tool calling, memory, and intelligence 


# 🤖 Gemini AI Applications using Google Gemini API

## 📌 Overview

This repository contains multiple Generative AI applications built using **Google Gemini API**, **Python**, and **Streamlit**.

The project demonstrates different capabilities of Gemini AI including:

* AI Chatbot
* Question Answering System
* Image Understanding using Gemini Vision
* Gemini API testing and experimentation

---

# 🚀 Applications Included

## 1. 🌐 Gemini AI Streamlit Application

### File:

`app.py`

### Description:

A Streamlit-based application that provides an interactive interface to communicate with Google Gemini AI.

### Features:

* User-friendly interface
* Gemini-powered responses
* Real-time AI interaction

### Output:

<img src="./Images/Output%20Images/App%20OUTPUT.png" width="800"/>

---

# 2. 💬 Gemini Chat Application

### File:

`chat.py`

### Description:

A conversational AI chatbot developed using Google Gemini API that allows users to interact with an AI assistant.

### Features:

* Natural language conversation
* AI-generated responses
* Real-time chatbot interaction

### Output:

<img src="./Images/Output%20Images/Chat%20Output.png" width="800"/>

---

# 3. ❓ Gemini Question Answering Application

### File:

`qachat.py`

### Description:

A Question Answering system that uses Gemini AI to understand user queries and generate accurate responses.

### Features:

* Question understanding
* AI-based answer generation
* Fast response generation

### Output:

<img src="./Images/Output%20Images/QACHAT%20Output.png" width="800"/>

---

# 4. 👁️ Gemini Vision Application

### File:

`vision.py`

### Description:

A multimodal AI application using Gemini Vision that analyzes uploaded images and provides intelligent descriptions.

### Features:

* Image upload
* Image analysis
* Visual question answering
* Multimodal AI capabilities

## Input Image:

<img src="./Images/Output%20Images/Vision1.png" width="600"/>

## Gemini Vision Output:

<img src="./Images/Output%20Images/Vision2.png" width="800"/>

---

# 5. 🧪 Gemini Model Testing

### File:

`testmodels.py`

### Description:

Used for testing Gemini models, checking API connectivity, and experimenting with different Gemini model responses.

---

# 6. 📚 Gemini Introduction

### File:

`gemini_intro.py`

### Description:

Basic implementation of Google Gemini API with Python.

Concepts covered:

* API configuration
* Model initialization
* Text generation

---

# 7. 📚 Gemini Introduction 1

### File:

`gemini_intro1.py`

### Description:

Additional examples demonstrating Gemini API usage and response generation.

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
├── Images/
│   └── Output Images/
│       ├── App OUTPUT.png
│       ├── Chat Output.png
│       ├── QACHAT Output.png
│       ├── Vision1.png
│       └── Vision2.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone <your-github-repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Load API key:

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
* Add `.env` inside `.gitignore`.
* Users need their own Gemini API key to run this project.

---

# 🎯 Future Improvements

* Add conversation memory
* Add voice interaction
* Deploy using Streamlit Cloud
* Add more Gemini multimodal features

---

# 👩‍💻 Author

**Ankita Shendge**

B.Tech Artificial Intelligence & Data Science
