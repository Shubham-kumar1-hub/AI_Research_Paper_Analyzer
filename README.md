# AI Research Paper Analyzer

AI Research Paper Analyzer is a simple GenAI project that helps users analyze research papers using LLMs and RAG (Retrieval-Augmented Generation). Users can upload a PDF research paper and generate summaries, research gaps, critical analysis, future suggestions, and also chat with the paper.

---

## Features

- Upload research papers in PDF format
- Extract text from PDFs using PyMuPDF
- Generate concise summaries
- Perform critical analysis
- Identify research gaps
- Suggest future research ideas
- Chat with the research paper using RAG
- Semantic search using FAISS vector database
- Embedding generation using Sentence Transformers
- Fast LLM responses using Groq API

---

## Tech Stack

- Python
- Streamlit
- Groq API
- FAISS
- Sentence Transformers
- PyMuPDF
- AWS EC2
- RAG (Retrieval-Augmented Generation)

---

## Project Architecture

```text
User Uploads PDF
        │
        ▼
PDF Text Extraction (PyMuPDF)
        │
        ▼
Text Chunking
        │
        ▼
Generate Embeddings
(Sentence Transformers)
        │
        ▼
Store Embeddings in FAISS
        │
        ▼
User Query / Analysis Request
        │
        ▼
Retrieve Relevant Chunks (RAG)
        │
        ▼
Send Context to Groq LLM
        │
        ▼
Generate Final Response
```

---

## Folder Structure

```text
AI_Research_Paper_Analyzer/
│
├── app.py
├── config.py
├── llm_utils.py
├── pdf_utils.py
├── rag_utils.py
├── requirements.txt
├── .env
└── temp_uploaded_pdfs/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Shubham-kumar1-hub/AI_Research_Paper_Analyzer.git
```

### Move into Project Folder

```bash
cd AI_Research_Paper_Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=llama-3.3-70b-versatile
```

---

## Run the Project

```bash
streamlit run app.py
```

---

## AWS Deployment

This project was deployed on AWS EC2 using Ubuntu Server and Streamlit.

### Deployment Link

http://52.90.158.35:8501

---

## Future Improvements

- Add support for multiple PDFs
- Persistent vector database storage
- Better UI design
- Add citation generation
- Add authentication system
- Dockerize the project
- Deploy using CI/CD pipeline

---

## GitHub Repository

GitHub Repo:  
https://github.com/Shubham-kumar1-hub/AI_Research_Paper_Analyzer

---

## Author

Shubham Kumar Jha
