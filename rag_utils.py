from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from config import settings


embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)


class RAGSystem:

    def __init__(self):
        self.index = None
        self.chunks = []

    def split_text_into_chunks(self, text):

        chunks = []

        chunk_size = settings.CHUNK_TARGET_CHAR_COUNT
        overlap = settings.CHUNK_OVERLAP_CHAR_COUNT

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start = end - overlap

        return chunks
    
    def create_vector_store(self, text):

        self.chunks = self.split_text_into_chunks(text)

        embeddings = embedding_model.encode(self.chunks)

        embeddings = np.array(embeddings).astype('float32')

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

    def retrieve_relevant_chunks(self, query, top_k=3):

        if self.index is None:
            return []

        query_embedding = embedding_model.encode([query])

        query_embedding = np.array(query_embedding).astype('float32')

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        retrieved_chunks = []

        for idx in indices[0]:
            if idx < len(self.chunks):
                retrieved_chunks.append(self.chunks[idx])

        return retrieved_chunks