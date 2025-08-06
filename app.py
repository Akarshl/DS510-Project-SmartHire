import streamlit as st
import os
import shutil
import tempfile
import pandas as pd
from scripts.resume_parser import extract_text
from scripts.preprocess import clean_text
from scripts.vectorizer import get_embedding
from torch.nn.functional import cosine_similarity

# Streamlit page setup
st.set_page_config(page_title="SmartHire Resume Ranking", layout="centered")
st.title("🤖 SmartHire: AI-Powered Resume Screening Tool")
st.markdown("Upload a job description and resumes (PDF/DOCX), and get ranked candidates based on relevance.")

# Input: Job description
job_desc = st.text_area("📄 Paste Job Description Below", height=200)

# Input: Resumes
uploaded_resumes = st.file_uploader(
    "📁 Upload Resumes (PDF or DOCX)",
    accept_multiple_files=True,
    type=["pdf", "docx"]
)

# Action button
if st.button("🔍 Rank Resumes"):
    if not job_desc or not uploaded_resumes:
        st.warning("⚠️ Please provide both a job description and at least one resume.")
    else:
        job_vec = get_embedding(clean_text(job_desc))
        results = []

        with st.spinner("Processing and ranking resumes..."):
            for file in uploaded_resumes:
                filename = file.name
                try:
                    # Ensure temp file has correct extension
                    file_ext = os.path.splitext(filename)[1]
                    with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as temp:
                        shutil.copyfileobj(file, temp)
                        temp_path = temp.name

                    # Extract, clean, embed, and compare
                    raw_text = extract_text(temp_path)
                    cleaned_text = clean_text(raw_text)
                    resume_vec = get_embedding(cleaned_text)
                    score = cosine_similarity(resume_vec, job_vec, dim=0).item()
                    results.append((filename, round(score, 4)))
                except Exception as e:
                    st.error(f"❌ Failed to process {filename}: {e}")

        # Display and download results
        if results:
            results.sort(key=lambda x: x[1], reverse=True)
            ranked_data = [
                {"Rank": i + 1, "Resume": name, "Score": score}
                for i, (name, score) in enumerate(results)
            ]
            df = pd.DataFrame(ranked_data)
            st.success("✅ Ranking completed!")
            st.dataframe(df, use_container_width=True)

            # Download CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results CSV",
                data=csv,
                file_name="ranked_resumes.csv",
                mime="text/csv"
            )
