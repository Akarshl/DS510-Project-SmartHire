import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def convert_txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    c = canvas.Canvas(pdf_path, pagesize=LETTER)
    width, height = LETTER
    margin = 40
    y = height - margin

    for line in lines:
        if y < margin:
            c.showPage()
            y = height - margin
        c.drawString(margin, y, line.strip())
        y -= 14  # Line spacing

    c.save()

def batch_convert_txts(input_dir='data/resumes/', output_dir='data/resumes_pdf/'):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            txt_path = os.path.join(input_dir, filename)
            pdf_path = os.path.join(output_dir, filename.replace('.txt', '.pdf'))
            convert_txt_to_pdf(txt_path, pdf_path)
            print(f"Converted {filename} → {os.path.basename(pdf_path)}")

if __name__ == "__main__":
    batch_convert_txts()
