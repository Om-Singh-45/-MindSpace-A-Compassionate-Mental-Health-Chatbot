from sentence_transformers import SentenceTransformer

# download model and cache it in a safer local folder
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    cache_folder="C:\\Users\\Shruti Singh\\Desktop\\hf_cache"
)

print("✅ Model downloaded successfully!")
