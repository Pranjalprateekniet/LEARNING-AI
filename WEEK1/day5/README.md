# AI Resume Screening & Candidate Ranking System

An LLM-powered Resume Screening System that automatically analyzes resumes, extracts structured candidate information, compares candidates against a job description, and ranks applicants based on their relevance.

The project demonstrates how Large Language Models (LLMs), Prompt Engineering, and Pydantic can be combined to automate the first stage of the recruitment process.

---

# Features

- Parse PDF and DOCX resumes
- Extract structured candidate information using an LLM
- Parse any Job Description (JD)
- Compare resumes against the JD
- Generate candidate match scores
- Explain why each score was assigned
- Highlight missing skills
- Suggest candidate improvements
- Rank all candidates automatically
- Works for any job role by simply changing the Job Description

---

# Tech Stack

- Python 3.12
- Groq API
- Pydantic
- PyPDF
- python-docx
- python-dotenv
- uv

---

# Project Structure

```
resume-screener/
│
├── resume_parser.py
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│   └── candidate3.docx
│
├── .env.example
├── README.md
├── pyproject.toml
└── uv.lock
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

Go inside the project

```bash
cd your-repository
```

Create a virtual environment

```bash
uv venv
source .venv/bin/activate
```

Install dependencies

```bash
uv sync
```

---

# Environment Variables

Copy the example file

```bash
cp .env.example .env
```

Open `.env` and add your Groq API Key

```env
GROQ_API_KEY=your_api_key_here
```

---

# How to Use

## Step 1

Place all candidate resumes inside the `resumes/` folder.

Example:

```
resumes/
    Alice.pdf
    Bob.docx
    Charlie.pdf
```

---

## Step 2

Open `resume_parser.py`

Locate the following variable:

```python
text = """
Your Job Description Here
"""
```

Replace it with the Job Description you want to evaluate resumes against.

Example:

```text
Software Engineer

Requirements

• Python
• Docker
• AWS
• SQL
• REST APIs
• Bachelor's Degree
```

If tomorrow you want to screen resumes for a Data Scientist, UI/UX Designer, HR Manager, Product Manager, or any other role, simply replace the Job Description with the new one.

No other code changes are required.

---

## Step 3

Run the project

```bash
python resume_parser.py
```

---

# Example Output

```
===========================
TOP 2 CANDIDATES
===========================

John Doe - 91%

Excellent Python experience
Strong cloud background
Matches 9 out of 10 required skills

-----------------------------------

Jane Smith - 84%

Strong backend profile
Missing Kubernetes experience

===========================
LOWEST 2 CANDIDATES
===========================

...
```

---

# Workflow

```
                Job Description
                        │
                        ▼
          Extract Job Requirements
                        │
                        ▼
         Read Resume (PDF / DOCX)
                        │
                        ▼
      Structured Resume Extraction
                        │
                        ▼
      Compare Resume vs Job Description
                        │
                        ▼
          Generate Match Score
                        │
                        ▼
      Rank All Candidates
                        │
                        ▼
         Display Best Candidates
```

---

# Supported Resume Formats

- PDF
- DOCX

---

# Current Limitations

- Uses an LLM API (internet connection required)
- Subject to API rate limits
- Sequential resume processing
- Supports only PDF and DOCX
- Job Description is currently provided directly in the source code

---

# Future Improvements

- Streamlit Web UI
- Upload Job Description from a text box or PDF
- Export results to Excel/CSV
- Batch asynchronous processing
- Retry mechanism for API rate limits
- Resume embeddings
- Semantic Search
- Docker deployment
- REST API version

---

# Learning Outcomes

This project demonstrates practical usage of

- Prompt Engineering
- Structured Outputs
- Pydantic
- LLM APIs
- Information Extraction
- Resume Parsing
- Candidate Ranking
- Python Automation

---

# License

MIT License