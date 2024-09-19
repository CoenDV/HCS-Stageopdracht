import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class SimpleRetriever:
    def __init__(self, documents):
        self.documents = documents
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self._build_index()

    def _build_index(self):
        # Create embeddings for the documents
        embeddings = self.model.encode(self.documents)
        dimension = embeddings.shape[1]

        # Create a FAISS index
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def retrieve(self, query, top_k=3):
        # Embed the query
        query_embedding = self.model.encode([query])

        # Search the FAISS index
        distances, indices = self.index.search(np.array(query_embedding), top_k)
        
        # Return the top_k documents
        return [self.documents[idx] for idx in indices[0]]

# Example usage
# documents = ["Document 1 text...", "Document 2 text...", ...]
# retriever = SimpleRetriever(documents)
# retriever.retrieve("query text")