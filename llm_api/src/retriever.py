from sentence_transformers import SentenceTransformer
from pymilvus import MilvusClient

class SimpleRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.milvus_client = MilvusClient(host='localhost', port='19530')


    def retrieve(self, query, top_k=3, relevance_threshold=0.5):
        # Embed the query
        query_embedding = self.model.encode([query])

        # Filter results based on distance
        param = {
            # use `L2` as the metric to calculate the distance
            "metric_type": "L2",
            "params": {
                # search for vectors with a distance smaller than 1.0
                "radius": 1.0,
                # filter out vectors with a distance smaller than or equal to the relevance_threshold
                "range_filter" : relevance_threshold
            }
        }

        # Search the collection
        res = self.milvus_client.search(
            collection_name="demo_collection",
            data=query_embedding,
            params=param,
            limit=top_k,
            output_fields=["text", "subject"]
        )

        return res