<div align="center">

# 🔍 CareerScan — AI Resume Analyzer

### *Upload your resume. Get your ATS score. Land the job.*

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LLaMA](https://img.shields.io/badge/LLaMA_3.3_70B-00A67E?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com)
[![Groq](https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge&logo=thunderbird&logoColor=white)](https://console.groq.com)

> Upload your resume and a job description — get an instant ATS score, keyword gap analysis, and HR-style feedback powered by LLaMA 3.3-70B.

</div>

## ✨ Features

- 📄 **Resume Parsing** — Extracts text from any PDF resume using pdfplumber
- 🤖 **HR Profile Review** — LLaMA 3.3-70B gives a professional HR-style evaluation of your resume
- 📊 **ATS Percentage Match** — See exactly how well your resume matches the job description
- 🔍 **Keyword Gap Detection** — Find missing keywords that ATS systems look for
- ⚡ **Fast Results** — Get structured feedback in under 4 seconds

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **AI Model** | LLaMA 3.3-70B via Groq API |
| **PDF Parsing** | pdfplumber |
| **Environment** | python-dotenv |

---

## 💡 How It Works

1. Paste the **job description** in the text box
2. Upload your **resume as PDF**
3. Choose an analysis mode:

| Mode | What You Get |
|---|---|
| 📋 Tell me about the resume | HR-style profile evaluation |
| 🚀 How can I improve my skills | Skill gap suggestions |
| 📊 Percentage Match | ATS score + missing keywords |

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Mahrang1/CareerScan.git
cd smart-resume-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup API key — create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free key → [console.groq.com](https://console.groq.com)

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit
groq
pdfplumber
python-dotenv
```

---

## 📁 Project Structure

```
├── app.py               # Main Streamlit app
├── .env                 # API key (not pushed to GitHub)
├── .env.example         # Template for API key
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🙋‍♀️ Built By

**Mahrang Riaz** — [github.com/Mahrang1](https://github.com/Mahrang1)

*Sir Syed University of Engineering and Technology, Karachi*

*Powered by LLaMA 3.3-70B via Groq API | Built with Streamlit*

---

<div align="center">

*Found this useful? Drop a ⭐ — it means a lot!* 😊

</div>
