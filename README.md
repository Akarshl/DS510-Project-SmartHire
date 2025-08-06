DS510-Project-SmartHire
# SmartHire AI-Powered Resume Screening Tool

An intelligent resume screening system that ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP) techniques like TF-IDF and Sentence-BERT. This tool helps recruiters automate the initial resume filtering process by computing semantic similarity scores between resume content and job descriptions.

# Features
 •	Parses and cleans resume data from CSV files or documents\
 •	Extracts relevant metadata such as email and phone number\
 •	Applies TF-IDF and Sentence-BERT for vectorization\
 •	Computes cosine similarity for ranking resumes\
 •	Outputs top-matching resumes for a given job description\
 •	JSON export and leaderboard-style relevance ranking

# Project Structure

├── data/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;← Dataset files (e.g., UpdatedResumeDataSet.csv)\
├── output/&emsp;&emsp;&emsp;&ensp;← Parsed JSON outputs\
├── src/&emsp;&emsp;&emsp;&emsp;← Source code\
│   ├── csv_resume_parser.py&emsp;← Resume parser for CSV format\
│   ├── tfidf_ranker.py&emsp;&emsp;&emsp;&emsp;&ensp;← TF-IDF based similarity ranking\
│   ├── bert_ranker.py&emsp;&emsp;&emsp;&emsp;&ensp;← Sentence-BERT based ranking (WIP)\
├── app.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;← (Optional) Streamlit/Flask UI\
├── requirements.txt&emsp;&emsp;← Python dependencies\
└── README.md

# Tech Stack
 •	Python 3.8+\
 •	pandas, nltk, scikit-learn\
 •	transformers (HuggingFace) for Sentence-BERT\
 •	PyPDF2, python-docx (if supporting file uploads)\
 •	Streamlit/Flask (optional UI)
