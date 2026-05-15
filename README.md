# AI Research Paper Analyzer with RAG

AI Research Paper Analyzer is a simple AI-powered web application that helps users analyze research papers in PDF format.

The project allows users to:
- Upload research papers in PDF format
- Generate summaries
- Perform critical analysis
- Identify research gaps
- Generate future research suggestions
- Chat with the uploaded research paper using RAG (Retrieval-Augmented Generation)

This project is built using Python, Streamlit, PyMuPDF, Groq LLM, Sentence Transformers, and FAISS Vector Database.

---

# Features

- Upload PDF research papers
- Extract text from PDF files
- AI-generated summaries
- Critical analysis generation
- Research gap identification
- Suggestions for future research
- RAG-based semantic retrieval
- Chat with research paper
- FAISS vector database integration
- Embedding generation using Sentence Transformers
- Handles large PDFs using chunking
- Simple Streamlit UI

---

# Technologies Used

- Python
- Streamlit
- PyMuPDF
- Groq API
- Llama 3
- Sentence Transformers
- FAISS
- NumPy
- python-dotenv

---

# Project Architecture

```text
AI_Research_Paper_Analyzer/
│
├── app.py
│   └── Main Streamlit application
│
├── config.py
│   └── Stores configurations and environment variables
│
├── pdf_utils.py
│   └── Handles PDF parsing and text extraction
│
├── llm_utils.py
│   └── Handles LLM analysis and question answering
│
├── rag_utils.py
│   └── Handles chunking, embeddings, vector database,
│       and semantic retrieval
│
├── requirements.txt
│   └── Required Python libraries
│
├── .env
│   └── Stores API keys and model settings
│
└── temp_uploaded_pdfs/
    └── Temporary uploaded PDF storage
```

---

# Project Workflow

```text
Upload PDF
    ↓
Extract Text from PDF
    ↓
Split Text into Chunks
    ↓
Generate Embeddings
    ↓
Store Embeddings in FAISS Vector DB
    ↓
Semantic Retrieval
    ↓
Send Relevant Chunks to Groq LLM
    ↓
Generate AI Response
```

---

# RAG Workflow

The project now uses RAG (Retrieval-Augmented Generation).

Instead of sending the entire PDF to the LLM, the system:
1. Splits the PDF into chunks
2. Creates embeddings
3. Stores embeddings in FAISS vector database
4. Retrieves only the most relevant chunks
5. Sends relevant chunks to the LLM

This improves:
- Response accuracy
- Speed
- Token efficiency
- Context relevance

---

# File Explanation

## 1. app.py

Main Streamlit application file.

Responsibilities:
- Handles UI
- Uploads PDFs
- Runs analysis
- Creates RAG pipeline
- Handles Chat with PDF
- Displays results

---

## 2. config.py

Stores:
- API keys
- Model names
- Chunk sizes
- Analysis options
- Upload directory

---

## 3. pdf_utils.py

Handles:
- PDF parsing
- Text extraction
- PDF validation
- PDF error handling

Main library used:
```python
import fitz
```

---

## 4. llm_utils.py

Handles:
- Groq API calls
- AI analysis generation
- Prompt engineering
- Chat with PDF answers

Main functions:
```python
get_llm_analysis()
```

```python
ask_question_about_paper()
```

---

## 5. rag_utils.py

Handles:
- Text chunking
- Embedding generation
- FAISS vector database
- Semantic retrieval

Main libraries:
```python
SentenceTransformer
faiss
numpy
```

---

# Installation Steps

## 1. Clone Repository

```bash
git clone https://github.com/Shubham-kumar1-hub/AI_Research_Paper_Analyzer.git
```

---

## 2. Move to Project Folder

```bash
cd AI_Research_Paper_Analyzer
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the project folder.

Add:

```env
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=llama-3.3-70b-versatile
```

---

# Run the Project

```bash
streamlit run app.py
```

---

# How to Use

1. Upload a PDF research paper
2. Select analysis types
3. Click "Analyze Paper"
4. View AI-generated analysis
5. Ask questions using Chat With Research Paper feature

---

# Analysis Types

- Summary
- Critical Analysis
- Research Gaps
- Suggestions for Future Research

---

# Chat With Research Paper

The project supports semantic question answering using RAG.

Example questions:
- What dataset was used?
- What methodology was used?
- What are the limitations?
- What are the future improvements?

The system retrieves relevant chunks from the vector database before sending them to the LLM.

---

# Dependencies

Main dependencies used:

```txt
streamlit
PyMuPDF
python-dotenv
groq==0.11.0
httpx==0.27.2
sentence-transformers
faiss-cpu
numpy
```

---

# Future Improvements

Possible future improvements:
- OCR support for scanned PDFs
- Citation generation
- Multi-document analysis
- Research paper comparison
- Export analysis as PDF/DOCX
- Cloud deployment
- Research recommendation system

---

# Limitations

- Scanned PDFs may not work properly
- Large PDFs may take more processing time
- Internet connection is required
- API key is required
- AI responses may not always be fully accurate

---

# Conclusion

AI Research Paper Analyzer with RAG is a beginner-friendly GenAI project that combines:
- PDF processing
- Vector databases
- Embeddings
- Semantic search
- Large Language Models

The project helped in understanding:
- RAG architecture
- Chunking
- Vector databases
- Embeddings
- Semantic retrieval
- LLM integration
- Streamlit application development

---

# GitHub Repository

https://github.com/Shubham-kumar1-hub/AI_Research_Paper_Analyzer
