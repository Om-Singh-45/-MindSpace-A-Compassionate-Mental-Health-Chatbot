from flask import Flask, request, jsonify, render_template
import requests
import traceback
import time
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# ---------------------------------------------------------
# 🔧 LOCAL LLM SETTINGS (Ollama)
# ---------------------------------------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"  # You can also use "phi3:mini" or "llama3"
# ---------------------------------------------------------

# ----- LOAD RAG KNOWLEDGE BASE -----
embedder = SentenceTransformer("all-MiniLM-L6-v2")

try:
    index = faiss.read_index("data/mental_health_index.faiss")
    texts = np.load("data/mental_health_texts.npy", allow_pickle=True)
    print("✅ RAG knowledge base loaded successfully.")
except Exception as e:
    print("⚠️ Could not load FAISS index, RAG will be disabled:", e)
    index = None
    texts = []


# ----- HELPER: RETRIEVE CONTEXT -----
def retrieve_context(query, k=3):
    """Find top relevant knowledge base entries for a given query."""
    if index is None or len(texts) == 0:
        return ""
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding, dtype="float32"), k)
    return "\n".join([texts[i] for i in I[0] if i < len(texts)])


# ----- ROUTES -----
@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please send a message."})

    # Retrieve relevant context from RAG
    context = retrieve_context(user_message)
    if context:
        print("\n🔍 Retrieved context:\n", context)

    # ---------------------------------------------------------
    # 🧠 IMPROVED STRUCTURED PROMPT FOR PHI (LOCAL MODEL)
    # ---------------------------------------------------------
    prompt = f"""
You are a compassionate mental health support chatbot. 
Keep your tone calm, caring, and emotionally supportive. 
Always keep your answers short (no more than 5 sentences) and well-structured.

RULES:
1. Never provide medical or diagnostic advice. 
2. If the user mentions suicidal thoughts, respond with empathy and urge them to contact a helpline.
3. Always end with a hopeful or comforting sentence.
4. Use this output format:

---
Emotional Understanding: (1 short empathetic sentence)
Practical Suggestion: (1 helpful, safe action the user can take)
Encouragement: (1 short positive or hopeful message)
---

Context (for reference):
{context}

User message:
"{user_message}"

Now provide your response following the format above.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.4,    # slightly lower for more focused tone
            "num_predict": 250     # shorter, cleaner responses
        }
    }

    headers = {"Content-Type": "application/json"}

    # Try twice in case first request times out
    for attempt in range(2):
        try:
            print(f"🕐 Sending request to Ollama (attempt {attempt + 1})...")
            resp = requests.post(OLLAMA_URL, json=payload, headers=headers, timeout=90)
            resp.raise_for_status()

            data = resp.json()
            reply = data.get("response", "").strip()

            if not reply:
                reply = "I'm here for you. Could you tell me more about what’s been on your mind?"

            print("🧠 Local LLM (Ollama) reply:", reply)
            return jsonify({"reply": reply})

        except requests.exceptions.ReadTimeout:
            print("⚠️ Ollama took too long to respond — retrying...")
            time.sleep(5)
            continue

        except requests.exceptions.RequestException as e:
            print("❌ HTTP error while connecting to Ollama:", e)
            traceback.print_exc()
            reply = "Sorry — I’m having trouble connecting to the local model right now."
            break

        except Exception as e:
            print("❌ Unexpected error:", e)
            traceback.print_exc()
            reply = "I’m here to listen. Could you tell me a bit more about how you feel?"
            break

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
