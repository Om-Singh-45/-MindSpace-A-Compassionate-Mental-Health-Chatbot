# 🧠 MindSpace: AI-Powered Mental Health Chatbot

> **“A safe space where empathy meets AI.”**  
> MindSpace is a local, privacy-first mental health companion chatbot designed to provide compassionate, structured emotional support using **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)** — all running **offline** via [Ollama](https://ollama.ai/).

---

## 🌟 Features

✅ **Emotionally Intelligent Responses** – Provides short, structured, empathetic answers (not medical advice).  
✅ **Privacy-Focused** – 100% offline using Ollama local models like *Mistral*, *Phi*, or *LLaMA3*.  
✅ **Context-Aware Chat** – Uses **FAISS** and **Sentence Transformers** for semantic similarity search (RAG).  
✅ **Structured Output Format** – Always replies with:
- 🩵 Emotional Understanding  
- 💡 Supportive Suggestion  
- 🌼 Encouragement  

✅ **Flask Web App** – Simple and elegant interface for real-time chat.  
✅ **Modular Codebase** – Easy to customize models, prompt style, and dataset.  

---

## 🏗️ Project Architecture

MindSpace/
│
├── app.py # Main Flask backend
├── templates/
│ └── chat.html # Frontend UI
├── data/
│ ├── mental_health_index.faiss # FAISS knowledge index
│ └── mental_health_texts.npy # Stored context texts
├── static/
│ └── style.css # Optional styling
├── requirements.txt # Python dependencies
└── README.md # Documentation (this file)


---

## ⚙️ Tech Stack

- **Backend:** Flask (Python)
- **Model Engine:** [Ollama](https://ollama.ai/)
- **LLMs Supported:** Mistral, Phi, LLaMA3, Gemma
- **Embedding Model:** SentenceTransformer (`all-MiniLM-L6-v2`)
- **Search Engine:** FAISS (Facebook AI Similarity Search)
- **Frontend:** HTML, CSS, JS (Flask Templates)

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Make sure you have:
- 🐍 Python 3.9+
- 🧠 [Ollama](https://ollama.ai/download) installed
- 💾 At least 8GB RAM (for local model inference)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/mindspace-chatbot.git
cd mindspace-chatbot

⚖️ Disclaimer

MindSpace is not a substitute for professional mental health care.
It offers emotional support and active listening, but not medical advice, diagnosis, or treatment.
If you or someone you know is in crisis, please reach out to a local helpline or trusted individual immediately.

---

## ❤️ Acknowledgements

- [Ollama](https://ollama.ai/) — for local LLM inference  
- [Sentence Transformers](https://www.sbert.net/) — for text embeddings  
- [FAISS](https://github.com/facebookresearch/faiss) — for efficient vector search  
- The open-source community — for providing free, safe mental health datasets  

---

## 📸 Screenshots (Optional)

<img width="1869" height="886" alt="Screenshot 2025-10-29 005444" src="https://github.com/user-attachments/assets/0254d2a9-f5b1-49af-984a-70473a24606f" />

<img width="1636" height="822" alt="Screenshot 2025-10-29 005934" src="https://github.com/user-attachments/assets/fd5d36dc-6437-4488-9c99-85564f0fc1e7" />
<img width="1456" height="869" alt="Screenshot 2025-10-29 005845" src="https://github.com/user-attachments/assets/2c64579f-0d1f-4885-a986-0132f66391fe" />
Breathing Exercise



---
