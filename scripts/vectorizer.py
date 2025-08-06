from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Returns a dense vector representation of the text
    """
    return model.encode(text, convert_to_tensor=True)
