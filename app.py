from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pdfplumber
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"{input}\n\nResume Text:\n{pdf_content}\n\nJob Description:\n{prompt}"
            }
        ],
        max_tokens=2000,
    )
    return completion.choices[0].message.content

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text.strip()
    else:
        raise FileNotFoundError("no file uploaded")

# Page config
st.set_page_config(page_title="smart resume analyzer - Smart Resume Analyzer", layout="wide")

# CSS
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0f0f0f;
    color: #e0e0e0;
}
[data-testid="stAppViewContainer"] {
    background-color: #0f0f0f;
}
[data-testid="stHeader"] {
    background-color: #0f0f0f;
}
h1, h2, h3 {
    color: #ffffff;
}
[data-testid="stTextArea"] textarea {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #333;
    border-radius: 8px;
}
[data-testid="stFileUploader"] {
    background-color: #1a1a1a;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 8px;
}
[data-testid="stButton"] button {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #444;
    border-radius: 8px;
    width: 100%;
    transition: background-color 0.2s ease;
}
[data-testid="stButton"] button:hover {
    background-color: #2a2a2a;
    border-color: #666;
    color: #ffffff;
}
.result-box {
    background-color: #1a1a1a;
    border: 1px solid #333;
    border-radius: 10px;
    padding: 20px;
    margin-top: 16px;
    color: #e0e0e0;
}
.footer {
    text-align: center;
    color: #555;
    font-size: 0.8rem;
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid #222;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("## Smart Resume Analyzer")
st.markdown("<p style='color:#888; margin-top:-12px;'>AI-powered resume analyzer — powered by LLaMA 3.3-70B</p>", unsafe_allow_html=True)
st.divider()

# Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("**Job Description**")
    input_text = st.text_area("", placeholder="Paste the job description here...", height=200, key="input", label_visibility="collapsed")

with col2:
    st.markdown("**Upload Resume (PDF)**")
    uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
    if uploaded_file is not None:
        st.success("PDF uploaded successfully")

st.divider()

# Buttons
st.markdown("**Choose Analysis**")
col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    submit1 = st.button("HR Profile Review")
with col_b2:
    submit2 = st.button("Skill Improvement")
with col_b3:
    submit4 = st.button("ATS Percentage Match")

# Prompts
input_prompt1 = """
You are an experienced HR with tech experience in the field of Data Science, Full Stack Web Development,
Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job description.
"""

input_prompt2 = """
You are a skilled career coach with expertise in tech roles. Review the resume and job description provided.
Suggest specific skills the candidate should learn or improve to better match this role.
Be practical and specific — mention courses, tools, or technologies they should focus on.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with deep understanding of Data Science,
Full Stack Web Development, and ATS functionality. Evaluate the resume against the provided job description.
Output format:
1. Match Percentage: X%
2. Missing Keywords: list them
3. Final Thoughts: brief summary
"""

# Results
if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing your resume..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.markdown("<div class='result-box'>" + response.replace("\n", "<br>") + "</div>", unsafe_allow_html=True)
    else:
        st.warning("Please upload your resume first.")

elif submit2:
    if uploaded_file is not None:
        with st.spinner("Finding skill gaps..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.markdown("<div class='result-box'>" + response.replace("\n", "<br>") + "</div>", unsafe_allow_html=True)
    else:
        st.warning("Please upload your resume first.")

elif submit4:
    if uploaded_file is not None:
        with st.spinner("Calculating ATS match..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.markdown("<div class='result-box'>" + response.replace("\n", "<br>") + "</div>", unsafe_allow_html=True)
    else:
        st.warning("Please upload your resume first.")

# Footer
st.markdown("<div class='footer'>Made by Mahrang Riaz | Sir Syed University of Engineering and Technology</div>", unsafe_allow_html=True)