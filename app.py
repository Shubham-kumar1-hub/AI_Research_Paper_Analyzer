import streamlit as st
import os
import uuid
import logging

from config import settings
from pdf_utils import extract_text_from_pdf, PDFParsingError

from llm_utils import (
    get_llm_analysis,
    ask_question_about_paper,
    LLMAnalysisError
)

from rag_utils import RAGSystem

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title=settings.PROJECT_NAME,
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown(
    """
    <style>

    .reportview-container .main .block-container{
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }

    .stButton>button{
        width:100%;
        border-radius:0.5rem;
    }

    .stMultiSelect [data-baseweb="tag"]{
        background-color:#0078D4;
        color:white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TITLE
# -----------------------------

st.title(
    f"🔬 {settings.PROJECT_NAME} (RAG Enabled)"
)

st.markdown(
    "Upload a research paper (PDF) for "
    "AI-powered analysis and semantic "
    "question answering using RAG."
)

st.markdown(
    f"Powered by Groq + Llama 3 "
    f"(Model: `{settings.LLM_MODEL}`)"
)

# -----------------------------
# SESSION STATE
# -----------------------------

if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = {}

if 'current_pdf_name' not in st.session_state:
    st.session_state.current_pdf_name = None

if 'error_message' not in st.session_state:
    st.session_state.error_message = None

if 'processing' not in st.session_state:
    st.session_state.processing = False

if 'paper_text' not in st.session_state:
    st.session_state.paper_text = None

if 'rag' not in st.session_state:
    st.session_state.rag = None

# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "📂 Choose a PDF Research Paper",
    type="pdf"
)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header(
    "⚙️ Analysis Configuration"
)

selected_analysis_types_display = st.sidebar.multiselect(

    "Select Analysis Types:",

    options=list(settings.ANALYSIS_OPTIONS.keys()),

    format_func=lambda x: settings.ANALYSIS_OPTIONS[x],

    default=["summary", "gaps"]
)

custom_model_name = st.sidebar.text_input(

    "Override LLM Model",

    value=settings.LLM_MODEL
)

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

analyze_button = st.button(
    "🚀 Analyze Paper",
    type="primary",
    disabled=st.session_state.processing
)

# -----------------------------
# STATUS PLACEHOLDERS
# -----------------------------

status_placeholder_main = st.empty()

status_placeholder_llm = st.empty()

progress_bar = st.empty()

# -----------------------------
# MAIN ANALYSIS FLOW
# -----------------------------

if analyze_button and uploaded_file is not None:

    if not selected_analysis_types_display:

        st.error(
            "⚠️ Please select at least one analysis type."
        )

    else:

        st.session_state.processing = True

        st.session_state.analysis_results = {}

        st.session_state.current_pdf_name = uploaded_file.name

        temp_file_path = os.path.join(

            settings.UPLOAD_DIR,

            f"{uuid.uuid4().hex}_{uploaded_file.name}"
        )

        try:

            # -----------------------------
            # SAVE PDF
            # -----------------------------

            with open(temp_file_path, "wb") as f:

                f.write(uploaded_file.getbuffer())

            logger.info(
                f"Temporary file created: {temp_file_path}"
            )

            # -----------------------------
            # PDF EXTRACTION
            # -----------------------------

            status_placeholder_main.info(
                "⏳ Extracting text from PDF..."
            )

            extracted_text = extract_text_from_pdf(
                temp_file_path
            )

            st.session_state.paper_text = extracted_text

            logger.info(
                f"Extracted text length: "
                f"{len(extracted_text)}"
            )

            progress_bar.progress(0.2)

            # -----------------------------
            # CREATE RAG SYSTEM
            # -----------------------------

            status_placeholder_main.info(
                "🧠 Creating RAG vector database..."
            )

            rag = RAGSystem()

            rag.create_vector_store(extracted_text)

            st.session_state.rag = rag

            logger.info(
                "RAG vector database created successfully."
            )

            progress_bar.progress(0.6)

            status_placeholder_main.success(
                "✅ Vector database created successfully."
            )
            # -----------------------------
            # ANALYSIS
            # -----------------------------

            total_llm_analyses = len(
                selected_analysis_types_display
            )

            for i, analysis_key in enumerate(
                selected_analysis_types_display
            ):

                analysis_display_name = (
                    settings.ANALYSIS_OPTIONS[
                        analysis_key
                    ]
                )

                status_placeholder_main.info(
                    f"✨ Running "
                    f"{analysis_display_name}..."
                )

                try:

                    analysis_result = get_llm_analysis(

                        extracted_text,

                        analysis_key,

                        model_name=(
                            custom_model_name
                            or settings.LLM_MODEL
                        ),

                        streamlit_status_placeholder=(
                            status_placeholder_llm
                        )
                    )

                    st.session_state.analysis_results[
                        analysis_key
                    ] = analysis_result

                except LLMAnalysisError as llm_err:

                    st.session_state.analysis_results[
                        analysis_key
                    ] = (
                        f"❌ Error: {str(llm_err)}"
                    )

                progress_bar.progress(

                    0.6 + (
                        0.4 * (
                            (i + 1)
                            / total_llm_analyses
                        )
                    )
                )

            status_placeholder_main.success(
                "✅ Analysis Complete"
            )

        except PDFParsingError as pdf_err:

            st.error(
                f"PDF Parsing Error: {str(pdf_err)}"
            )

        except Exception as e:

            st.error(
                f"Unexpected Error: {str(e)}"
            )

        finally:

            if os.path.exists(temp_file_path):

                os.remove(temp_file_path)

            st.session_state.processing = False

# -----------------------------
# ANALYSIS RESULTS
# -----------------------------

if (
    st.session_state.analysis_results
    and st.session_state.current_pdf_name
):

    st.markdown("---")

    st.header(

        f"📊 Analysis Results for "
        f"{st.session_state.current_pdf_name}"
    )

    for analysis_key, result_text in (

        st.session_state.analysis_results.items()

    ):

        display_name = (

            settings.ANALYSIS_OPTIONS.get(

                analysis_key,

                analysis_key.replace(
                    "_",
                    " "
                ).title()
            )
        )

        with st.expander(
            f"**{display_name}**",
            expanded=True
        ):

            st.markdown(
                result_text,
                unsafe_allow_html=True
            )

# -----------------------------
# CHAT WITH PDF
# -----------------------------

if st.session_state.paper_text:

    st.markdown("---")

    st.header(
        "💬 Chat With Research Paper"
    )

    user_question = st.text_input(
        "Ask a question about the paper"
    )

    ask_button = st.button(
        "Ask Question"
    )

    if ask_button:

        if not user_question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Generating Answer..."
            ):

                retrieved_chunks = (
                st.session_state.rag
                .retrieve_relevant_chunks(
                    user_question
                )
            )

            context = "\n\n".join(
                retrieved_chunks
            )

            answer = ask_question_about_paper(

                context,

                user_question,

                model_name=(
                    custom_model_name
                    or settings.LLM_MODEL
                )
            )

            st.subheader("Answer")

            st.write(answer)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
    "ℹ️ Analysis quality depends on "
    "PDF text quality and LLM "
    "capabilities."
)