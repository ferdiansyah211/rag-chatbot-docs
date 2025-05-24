# chatbot.py
import os
import faiss
import pickle
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # atau e5-base, bge-small-en

def load_documents(folder="documents"):
    docs = []
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, filename))
            docs.extend(loader.load())
    return docs

def create_vector_index():
    docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding_model.encode(texts)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(embeddings)

    faiss.write_index(index, "index.faiss")
    with open("texts.pkl", "wb") as f:
        pickle.dump(texts, f)

    print("✅ Embedding selesai & disimpan.")

if __name__ == "__main__":
    create_vector_index()
