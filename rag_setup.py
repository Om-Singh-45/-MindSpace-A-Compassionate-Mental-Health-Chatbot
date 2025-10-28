from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model to create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load your text data
with open("data/mental_health_knowledge.txt", "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f.readlines() if line.strip()]

# Create embeddings
embeddings = model.encode(texts)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings, dtype="float32"))

# Save everything
faiss.write_index(index, "data/mental_health_index.faiss")
np.save("data/mental_health_texts.npy", np.array(texts))

print("✅ Knowledge base indexed and saved!")
