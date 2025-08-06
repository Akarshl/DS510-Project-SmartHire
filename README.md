
# SmartHire: AI-Powered Resume Screening Tool

SmartHire is an AI-powered application that automates the process of screening and ranking resumes based on a given job description. It uses state-of-the-art NLP models like Sentence-BERT to compute semantic similarity between resumes and job requirements, helping recruiters streamline candidate selection.

---

##  Features

-  Semantic ranking of resumes using Sentence-BERT embeddings
-  Supports `.pdf` and `.docx` resume files
-  Upload job descriptions and resumes directly through a web UI
-  Displays ranked resumes with similarity scores
-  Option to download the ranking as a CSV file
-  Built with Python, Streamlit, PyMuPDF, and Hugging Face Transformers

---

## Project Structure

```
resume_screening_ai/
├── data/
│   ├── job_description.txt        # Sample job description
│   ├── resumes/                   # Optional: original .txt resumes
│   └── resumes_pdf/               # Converted resumes in PDF format
│
├── output/
│   └── ranked_resumes.csv         # Final output (generated)
│
├── scripts/
│   ├── main.py                    # CLI-based pipeline
│   ├── resume_parser.py           # PDF/DOCX text extractor
│   ├── preprocess.py              # Text cleaning and stopword removal
│   ├── vectorizer.py              # Sentence-BERT embedding
│   └── ranker.py                  # Similarity calculation + ranking
│
├── app.py                         # Streamlit web app
├── convert_txt_to_pdf.py          # Converts .txt resumes to .pdf
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smarthire.git
cd smarthire
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run

### Option 1: Run the Streamlit Web App

```bash
streamlit run app.py
```

### Option 2: Run via Command Line

Make sure you have:
- Resumes in `data/resumes_pdf/`
- A job description in `data/job_description.txt`

Then run:

```bash
python scripts/main.py
```

---

## Sample Output

| Rank | Resume                        | Score |
|------|-------------------------------|-------|
| 1    | resume_2_Data_Science.pdf     | 0.87  |
| 2    | resume_5_Software_Engineer.pdf| 0.79  |
| 3    | resume_10_ML_Engineer.pdf     | 0.72  |

---

## Dependencies

- `streamlit`
- `torch`
- `sentence-transformers`
- `PyMuPDF` (`fitz`)
- `python-docx`
- `pandas`
- `nltk`
- `reportlab`

You can install them all using:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- Resume preview inside the app
- Upload job descriptions via file
- Deploy on Streamlit Cloud
- Filter top N resumes or by threshold score
- Visual analytics (e.g., score distribution)

---
