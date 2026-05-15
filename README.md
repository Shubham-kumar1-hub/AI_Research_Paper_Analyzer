# AI Research Paper Analyzer

AI Research Paper Analyzer is a simple AI-powered web application that helps users analyze research papers in PDF format.

The user can upload a research paper and generate:
- Summary
- Critical Analysis
- Research Gaps
- Suggestions for Future Research

This project is built using Python, Streamlit, PyMuPDF, and Groq LLM.

---

# Features

- Upload PDF research papers
- Extract text from PDF files
- Generate AI-based summaries
- Perform critical analysis
- Identify research gaps
- Generate future research suggestions
- Handles large PDFs using chunking
- Simple and easy-to-use Streamlit UI

---

# Technologies Used

- Python
- Streamlit
- PyMuPDF
- Groq API
- Llama 3 Model
- python-dotenv
- Logging

---

# Project Architecture

```text
AI_Research_Paper_Analyzer/
│
├── app.py
│   └── Main Streamlit application file
│
├── config.py
│   └── Stores project configurations and environment variables
│
├── pdf_utils.py
│   └── Handles PDF text extraction
│
├── llm_utils.py
│   └── Handles chunking and AI analysis using Groq LLM
│
├── requirements.txt
│   └── Required Python libraries
│
├── .env
│   └── Stores Groq API key and model name
│
└── temp_uploaded_pdfs/
    └── Temporary folder for uploaded PDFs
```

---

# Project Workflow

```text
User uploads PDF
        ↓
PDF is saved temporarily
        ↓
Text is extracted from PDF
        ↓
Extracted text is split into chunks
        ↓
Chunks are sent to Groq LLM
        ↓
AI generates analysis
        ↓
Results are displayed on Streamlit UI
```

---

# File Explanation

## 1. app.py

This is the main file of the project.

Responsibilities:
- Creates Streamlit web interface
- Uploads PDF files
- Handles user interaction
- Displays progress and results
- Calls PDF extraction functions
- Calls AI analysis functions

Main functions:
- Upload PDF
- Select analysis type
- Run AI analysis
- Display results

---

## 2. config.py

This file contains all project settings.

It loads environment variables using:

```python
load_dotenv()
```

Main settings:
- Project name
- Groq API key
- LLM model name
- Upload folder
- Chunk size
- Analysis options

Example:

```python
ANALYSIS_OPTIONS = {
    "summary": "Generate a concise summary of the research paper.",
    "critical_analysis": "critical Analysis",
    "gaps": "Research Gaps",
    "suggestions": "Suggestions for Future Research",
}
```

---

## 3. pdf_utils.py

This file handles PDF parsing and text extraction.

Main library used:

```python
import fitz
```

Main function:

```python
extract_text_from_pdf()
```

Responsibilities:
- Check if PDF exists
- Open PDF
- Extract text from pages
- Combine extracted text
- Handle PDF parsing errors

Custom Exception:

```python
PDFParsingError
```

---

## 4. llm_utils.py

This file handles AI analysis using Groq API.

Main responsibilities:
- Split large text into chunks
- Send chunks to LLM
- Generate AI analysis
- Handle retries and API errors

Main functions:

```python
split_text_into_chunks()
```

```python
get_llm_analysis()
```

Supported analysis types:
- Summary
- Critical Analysis
- Research Gaps
- Suggestions

---

# Why Chunking is Used

Research papers are usually very large.

LLMs cannot process extremely large text at once because of token limits.

So the extracted text is divided into smaller chunks.

Example:

```text
Full PDF Text
    ↓
Chunk 1
Chunk 2
Chunk 3
```

Each chunk is analyzed separately by the AI model.

---

# Installation Steps

## 1. Clone the Repository

```bash
git clone https://github.com/Shubham-kumar1-hub/AI_Research_Paper_Analyzer.git
```

---

## 2. Move to the Project Folder

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

Add the following variables:

```env
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=llama-3.3-70b-versatile
```

Replace:

```env
your_groq_api_key
```

with your actual Groq API key.

---

# Run the Project

Run the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, the application will open in your browser.

---

# How to Use

1. Open the application in browser
2. Upload a PDF research paper
3. Select analysis type from sidebar
4. Click on "Analyze Paper"
5. Wait for processing
6. View generated analysis

---

# Analysis Types

## 1. Summary

Generates a concise summary of the research paper.

---

## 2. Critical Analysis

Analyzes strengths, weaknesses, methodology, and contribution.

---

## 3. Research Gaps

Identifies missing areas and possible gaps in research.

---

## 4. Suggestions

Provides suggestions for future research and improvements.

---

# Error Handling

The project handles:
- Missing PDF files
- Empty PDFs
- API errors
- Invalid analysis types
- Empty AI responses

Custom exceptions used:

```python
PDFParsingError
LLMAnalysisError
```

---

# Limitations

- Scanned PDFs may not work properly
- Large PDFs take more processing time
- Internet connection is required
- Groq API key is required
- AI output may not always be fully accurate

---

# Future Improvements

Possible future improvements:
- Add OCR support
- Export results as PDF or DOCX
- Add database support
- Add user authentication
- Add multiple PDF upload support
- Improve UI design
- Add citation generation

---

# Conclusion

AI Research Paper Analyzer helps students and researchers quickly understand research papers using AI.

The project extracts text from PDFs and generates different types of AI-based analysis using Groq LLM.

This project was developed as a learning-based AI application using:
- Python
- Streamlit
- PyMuPDF
- Groq API
- Llama 3 Model
