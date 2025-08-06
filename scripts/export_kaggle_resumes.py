import pandas as pd
import os

df = pd.read_csv('data/UpdatedResumeDataSet.csv')
output_dir = 'data/resumes/'

os.makedirs(output_dir, exist_ok=True)

for i, row in df.iterrows():
    filename = f"resume_{i}_{row['Category'].strip().replace(' ', '_')}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(row['Resume'])
