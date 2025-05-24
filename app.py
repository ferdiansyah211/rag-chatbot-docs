# app.py
from flask import Flask, request, jsonify
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.llms import Ollama

# Load index & teks
index = faiss.read_index("index.faiss")
with open("texts.pkl", "rb") as f:
    texts = pickle.load(f)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
llm = Ollama(model="mistral")

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Pertanyaan tidak boleh kosong"}), 400

    query_vec = embedding_model.encode([question])
    D, I = index.search(query_vec, k=3)
    context = "\n\n".join([texts[i] for i in I[0]])

    prompt = f"""
    Kamu adalah asisten kebijakan perusahaan. Jawablah pertanyaan berikut hanya berdasarkan dokumen:

    ===KONTEKS===
    {context}

    ===PERTANYAAN===
    {question}

    Jawab dengan jelas dan singkat. Sebutkan sumber bila perlu.
    """

    response = llm(prompt)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
