from scripts.ranker import rank_resumes

# Read the job description
job_desc_path = "data/job_description.txt"
with open(job_desc_path, "r", encoding="utf-8") as f:
    job_description = f.read()

# Folder with converted PDF resumes
resume_folder = "data/resumes_pdf/"

# Run the ranking process
rank_resumes(resume_folder, job_description)
