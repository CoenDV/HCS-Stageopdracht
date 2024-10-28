from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    top_k: int = 6
    relevance_threshold: float = 0.5

class Document:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text