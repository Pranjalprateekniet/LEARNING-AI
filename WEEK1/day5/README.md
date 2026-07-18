# AI Resume Screening & Candidate Ranking System

An LLM-powered resume screening system that automatically analyzes resumes, extracts structured candidate information, compares candidates against a job description, and ranks them based on relevance.

The project demonstrates how Large Language Models can automate parts of the recruitment pipeline using structured outputs with Pydantic.

---

## Features

- Parse PDF and DOCX resumes
- Extract structured candidate information using an LLM
- Parse job descriptions
- Compare resumes against job requirements
- Generate candidate match scores
- Explain why each score was assigned
- Suggest improvements for each candidate
- Rank candidates automatically
- Supports multiple resumes in a single run

---

## Workflow

```text
                Job Description
                       │
                       ▼
              Parse Job Requirements
                       │
                       ▼
        ┌─────────────────────────┐
        │                         │
        ▼                         ▼
 Read Resume 1              Read Resume 2 ...
        │                         │
        ▼                         ▼
 Structured Resume Extraction (LLM)
        │
        ▼
 Candidate Evaluation (LLM)
        │
        ▼
 Match Score
        │
        ▼
 Candidate Ranking
```

---

## Tech Stack

- Python 3.12
- Groq API
- Pydantic
- python-dotenv
- PyPDF
- python-docx
- uv

---

## Project Structure

```
resume_parser.py
resumes/
    resume1.pdf
    resume2.pdf
    resume3.docx
.env
README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/repository.git
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

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

---

## Running

```bash
python resume_parser.py
```

---

## Example Output

```
Preprocessing: Resume1.pdf

Score: 72%

Top Candidate

Name:
Ashish Raj

Matching Skills:
- Python
- C++
- AWS
- Docker
- Kubernetes

Missing Skills:
- SQL
- Open Source Contributions

Verdict:
Strong technical profile with relevant DevOps experience.

------------------------------------

Preprocessing: Resume2.pdf

Score: 55%

Verdict:
Good programming foundation but lacks cloud and production experience.
```

---

## Structured Output

The project uses **Pydantic** to enforce a consistent schema returned by the LLM.

Example:

```json
{
  "candidate_name": "John Doe",
  "matching_skills": [
    "Python",
    "Docker"
  ],
  "missing_important_skills": [
    "AWS",
    "CI/CD"
  ],
  "overall_match_percentage": 72,
  "final_verdict": "...",
  "improvement_pointers": [
    "...",
    "..."
  ]
}
```

---

## Current Limitations

- Depends on LLM quality
- Uses prompt engineering instead of embeddings
- Sequential resume processing
- Subject to API rate limits
- Supports PDF and DOCX only

---

## Future Improvements

- Resume embeddings using vector databases
- Semantic search
- Streamlit web interface
- Batch processing with async requests
- Retry mechanism for API rate limits
- ATS-style dashboard
- Export results to CSV or Excel
- Docker deployment

---

## Learning Outcomes

This project demonstrates practical use of:

- Prompt Engineering
- Structured Outputs
- Pydantic
- LLM Pipelines
- Resume Parsing
- Information Extraction
- Candidate Ranking
- Python Automation

---

## License

MIT License