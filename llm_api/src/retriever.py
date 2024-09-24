from sentence_transformers import SentenceTransformer
from pymilvus import MilvusClient

class SimpleRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.milvus_client = MilvusClient(host='localhost', port='19530')


    def retrieve(self, query, top_k=6, relevance_threshold=0.5):
        # Embed the query
        query_embedding = self.model.encode([query])

        # Define the search parameters
        search_params = {
            "metric_type": "L2",
            "params": {
                "radius": relevance_threshold,
            }
        }

        # Search the collection
        res = self.milvus_client.search(
            collection_name="demo_collection",
            data=query_embedding,
            params=search_params,
            limit=top_k,
            output_fields=["text", "subject"]
        )

        return res