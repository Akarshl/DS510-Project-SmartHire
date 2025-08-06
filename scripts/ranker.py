from torch.nn.functional import cosine_similarity
import pandas as pd
import os
from scripts.resume_parser import extract_text
from scripts.preprocess import clean_text
from scripts.vectorizer import get_embedding

def rank_resumes(resume_folder, job_description_text):
    job_vec = get_embedding(clean_text(job_description_text))

    results = []

    for filename in os.listdir(resume_folder):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            filepath = os.path.join(resume_folder, filename)
            try:
                raw_text = extract_text(filepath)
                cleaned_text = clean_text(raw_text)
                resume_vec = get_embedding(cleaned_text)

                score = cosine_similarity(resume_vec, job_vec, dim=0).item()
                results.append((filename, score))
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Sort by similarity score (high to low)
    results.sort(key=lambda x: x[1], reverse=True)

    # Create DataFrame with Rank column
    ranked_data = []
    for idx, (filename, score) in enumerate(results, start=1):
        ranked_data.append({"Rank": idx, "Resume": filename, "Score": round(score, 4)})

    df = pd.DataFrame(ranked_data, columns=["Rank", "Resume", "Score"])

    # Save output
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/ranked_resumes.csv", index=False)
    print("\n Ranked resumes saved to output/ranked_resumes.csv")
    print(df)
