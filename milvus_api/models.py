from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    top_k: int = 6
    relevance_threshold: float = 0.5