import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    PROJECT_NAME: str = "AI Research Paper Analyzer"
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")

    UPLOAD_DIR: str = "temp_uploaded_pdfs"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensures directory exists

    ANALYSIS_OPTIONS = {
        "summary": "Generate a concise summary of the research paper.",
        "critical_analysis": " critical Analysis",
        "gaps": " Research Gaps",
        "suggestions": "Suggestions for Future Research",
    }

    # Target characters per chunk. ~4 chars/token. Aim for ~4000-5000 tokens per chunk payload.
    # If prompt is ~1000-1500 tokens, text chunk should be ~2500-3500 tokens.
    # 3000 tokens * 4 chars/token = 12000 characters per chunk.
    CHUNK_TARGET_CHAR_COUNT: int = 12000
    CHUNK_OVERLAP_CHAR_COUNT: int = 500 # Overlap to maintain context between chunks

settings = settings()
print(f"Project Name: {settings.PROJECT_NAME}")
print(f"analysis_options: {settings.ANALYSIS_OPTIONS['summary']}")

if not settings.GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables. Please set it before running the application.")
