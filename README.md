```markdown
# 📌 RAG Q&A System Using LangChain — YouTube Video Question Answering

This is a **Retrieval-Augmented Generation (RAG) application** built with **Streamlit** that lets users paste a YouTube video link and ask questions about its content. The system extracts video transcripts, creates embeddings using HuggingFace Sentence Transformers, stores them in a FAISS vector database, performs semantic search, and generates accurate answers using OpenAI LLMs through LangChain.

---

## 🚀 Overview

Instead of watching long YouTube videos, users can simply:
1. Paste a YouTube video link  
2. Type a question about the content  
3. Receive an accurate AI-generated answer supported by transcript excerpts  

The system is ideal for long podcasts, lectures, workshops, tutorials, tech talks, interviews, seminars, and educational videos.

---

## ✨ Features

- 🎥 YouTube transcript extraction
- 🧠 Retrieval-Augmented Generation pipeline
- 🤖 OpenAI LLM answer generation via LangChain
- 📝 HuggingFace Sentence-Transformer embeddings
- ⚡ Fast similarity search using FAISS vector database
- 🔎 Smart chunking with `RecursiveCharacterTextSplitter`
- 🖥️ User-friendly Streamlit interface

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| UI | Streamlit |
| RAG Framework | LangChain |
| LLM | OpenAI (ChatOpenAI) |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Store | FAISS |
| Transcript Loader | YouTube Transcript API |
| Language | Python |

---

## 📂 Project Structure

```

📦 rag_using_langchain
├─ 📜 app.py                        # Main Streamlit application
├─ 📜 requirements.txt              # Dependencies
├─ 📜 rag_using_langchain.ipynb     # Notebook for testing and exploration
└─ 📜 README.md                     # Documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/<your-username>/rag-using-langchain.git
cd rag-using-langchain
````

### 2️⃣ Create virtual environment

```bash
conda create -n rag python=3.11 -y
conda activate rag
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🕹️ Usage

1. Open `http://localhost:8501` in your browser
2. Paste a YouTube video link
3. Ask any question about the video content
4. View concise answers with relevant transcript context

---

## 🚧 Future Enhancements

* Support for PDFs and website URLs
* Multi-video knowledge merging
* Local LLM support (LLaMA, Mistral)
* Chat history and memory
* Export response as PDF/TXT

---

## 🤝 Contributing

Contributions are welcome!
To contribute:

1. Fork this repository
2. Create a feature branch
3. Commit and push
4. Open a pull request

---

## ⭐ Support

If this project was helpful, please **give it a star ⭐ on GitHub** — it motivates further development!
