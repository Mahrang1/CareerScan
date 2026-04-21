# 🎯 CareerScan — AI Resume Analyzer

> Upload your resume and a job description — get an instant ATS score, keyword gap analysis, and HR-style feedback powered by LLaMA 3.3-70B.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-00A67E?style=flat)
![LLaMA](https://img.shields.io/badge/LLaMA_3.3_70B-purple?style=flat)

---

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
| Frontend | Streamlit |
| AI Model | LLaMA 3.3-70B via Groq API |
| PDF Parsing | pdfplumber |
| Environment | python-dotenv |

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Mahrang1/smart-resume-analyzer.git
cd smart-resume-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Setup API key — create a `.env` file:**
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free key → [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
groq
pdfplumber
python-dotenv
```

---

## 💡 How It Works

1. Paste the **job description** in the text box
2. Upload your **resume as PDF**
3. Choose an analysis mode:
   - **Tell me about the resume** — HR-style profile evaluation
   - **How can I improve my skills** — skill gap suggestions
   - **Percentage Match** — ATS score with missing keywords

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

---

<p align="center">Powered by LLaMA 3.3-70B via Groq API | Built with Streamlit</p>
