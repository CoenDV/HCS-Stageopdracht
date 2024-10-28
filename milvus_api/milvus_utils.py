from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer
from glob import glob

from models import SearchRequest

class milvus_utils:
    def __init__(self, uri, port):
        self.uri = uri
        self.port = port
        self.milvus_client = MilvusClient(
            uri=self.uri,
            port=self.port,
        )
        self.model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/.cache')
        
### LOAD DOCUMENTS FUNCTION ###

    def load_documents(self):
        # create collection
        if self.milvus_client.has_collection("HCS_Insurance"):
            self.milvus_client.drop_collection("HCS_Insurance")

        self.milvus_client.create_collection(
            collection_name="HCS_Insurance", 
            dimension=384,
            metric_type="IP",
            index_type="IVF_FLAT",
        )

        # prepare documents
        print("Preparing documents...")
        docs = []

        for file_path in glob("./documents/*.txt", recursive=True):
            with open(file_path, "r") as file:
                file_text = file.read()
                docs.append(file_text)
        vectors = self.model.encode(docs)

        data = [
            {"id": i, "vector": vectors[i], "text": docs[i], "subject": "insurance"}
            for i in range(len(vectors))
        ]

        # insert data
        print("Inserting data...")
        res = self.milvus_client.insert(collection_name="HCS_Insurance", data=data)
        print(self.milvus_client.describe_collection("HCS_Insurance"))
        print(res)

        return {"response": "Data prepared successfully"}
    
### SEARCH FUNCTION ###

    def search(self, request: SearchRequest):
        query_embedding = self.model.encode([request.query])

        search_params = {
            "metric_type": "IP", # Inner Product, a way of measuring similarity
            "params": {
            "radius": request.relevance_threshold # Only return documents relevant to the query
            }
        }

        result = self.milvus_client.search(
            collection_name="HCS_Insurance", 
            data=query_embedding,
            limit=request.top_k,
            search_params=search_params,
            output_fields=["text"]
        )

        return result