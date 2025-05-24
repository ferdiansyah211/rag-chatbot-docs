# 🧠 Company Policy Assistant

An intelligent local chatbot that can answer employee questions about internal company policies. This system leverages a local Large Language Model (LLM) via [Ollama](https://ollama.com) and uses Retrieval-Augmented Generation (RAG) to respond with accurate, document-based answers.

---

## 🚀 Features

- 📄 Reads and processes local PDF policy documents.
- 🔍 Answers questions based on document content.
- 🔒 Fully local — documents and data are **not uploaded to the cloud**.
- ⚡ Uses local AI models via Ollama (e.g., Mistral, LLaMA3, Command-R).
- 🔌 Accessible via REST API (e.g., with Postman or other clients).

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask (REST API framework)
- LangChain (RAG pipeline)
- FAISS (vector database for semantic search)
- Ollama (to run local LLMs)
- PyMuPDF / PDFLoader (for PDF document reading)

---

## 📁 Project Structure

```
.
├── app.py                # Flask API
├── chatbot.py            # Initial document embedding process
├── data/                 # Folder containing policy PDFs
├── index/                # Folder for FAISS index storage
├── requirements.txt      # Python dependencies
```

---

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Ollama and run a local model
```bash
ollama run mistral
# or
ollama run command-r
```

### 3. Embed documents (first-time setup)
```bash
python chatbot.py
```

### 4. Start the Flask API
```bash
python app.py
```

---

## 🧪 Example Usage (Postman)

**Endpoint**: `POST /ask`

**Request body**:
```json
{
  "question": "What is the annual leave policy at this company?"
}
```

**Response**:
```json
{
  "answer": "According to kebijakan.pdf, employees are entitled to 12 days of paid leave annually..."
}
```

---

## 📁 Adding New Documents

1. Place new PDF files in the `data/` folder.
2. Re-run `chatbot.py` or use an endpoint (if available) to update the FAISS index dynamically.

---

## 🔐 Privacy & Security

- All files and computations remain **entirely on your machine**.
- Ideal for internal enterprise systems or on-premise environments.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! You can extend this project by adding:

- A web UI
- File upload endpoints
- Integration with HR/internal systems

Feel free to open an issue or PR.

---

## 📄 License

This project is licensed under the MIT License.

---