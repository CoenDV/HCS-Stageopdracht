from sentence_transformers import SentenceTransformer
from pymilvus import MilvusClient

class SimpleRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.milvus_client = MilvusClient(host='localhost', port='19530')


    def retrieve(self, query, top_k=6, relevance_threshold=0.5):
        query_embedding = self.model.encode([query])

        search_params = {
            "metric_type": "IP", # Inner Product, a way of measuring similarity
            "params": {
                "radius": relevance_threshold # Only return documents relevant to the query
            }
        }

        result = self.milvus_client.search(
            collection_name="demo_collection", 
            data=query_embedding,
            limit=top_k,
            search_params=search_params,
            output_fields=["text"]
        )

        return result