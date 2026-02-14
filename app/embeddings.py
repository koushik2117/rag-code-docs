from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(docs):
    embeddings = model.encode(docs)
    index = faiss.IndexFlatL2(384)
    index.add(np.array(embeddings))
    return index
